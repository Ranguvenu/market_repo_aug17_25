import sys
sys.path.append('/var/www/html/myproject/')
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
import pyotp, time
from config import *
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
import mysql.connector

# Define a global variable to store the response
RESPONSE_DATA = None
TOKENS = []
OPTION_LTP = []
I = 0
BEST_OPTION = None
TOKENS_WITHNAMES = None

def pickup_fromstream(obj=False, data=False, type  = False):
    global TOKENS_WITHNAMES
    global I
    if type == False:
        type = "CE"
    # captured_output = sys.stdout = sys.stderr = open('alive/entries.txt', 'a')

    if obj == False or data == False:
        obj = SmartConnect(api_key="yWjMIfbo")
        # login api call
        data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
    # refreshToken = data['data']['refreshToken']

    AUTH_TOKEN = data['data']['jwtToken']
    API_KEY = "yWjMIfbo"
    CLIENT_CODE = "V280771"
    FEED_TOKEN = data['data']['feedToken']
    correlation_id = "abc123"
    action = 1
    mode = 1
    # ranger_options = ranger_options_tokens(obj)
    # TOKENS_WITHNAMES = ranger_options[1]
    # token_collection = ranger_options[0]

    TOKENS_WITHNAMES, token_list = get_valid_options(type)
    token_collection = [{
        "exchangeType": 2,
        "tokens": token_list
    }]

    # retry_strategy = 0 for simple retry mechanism
    sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN, max_retry_attempt=0, retry_strategy=0, retry_delay=10, retry_duration=30)

    # Initialize TOKENS and OPTION_LTP outside the function
    I = 0

    def on_data(wsapp, message):
        global RESPONSE_DATA
        global TOKENS
        global OPTION_LTP
        global I
        global BEST_OPTION

        logger.info("Ticks: {}".format(message))


        RESPONSE_DATA = message
        print('dsdkdksnkd')

        token = RESPONSE_DATA['token']  # Assuming the key for token is 'token'
        last_traded_price = RESPONSE_DATA['last_traded_price']  # Assuming the key for last traded price is 'last_traded_price'
        if RESPONSE_DATA['token'] not in TOKENS:
            print("in appending:")
            TOKENS.append(token)
            OPTION_LTP.append({token: last_traded_price / 100})
            I += 1
            if I >= 15:
                I = 0
                close_connection()
                TOKENS = []
                # print("best option", best_option_fromlive(OPTION_LTP))
                # close
                # _connection()
                # exit()
                BEST_OPTION = best_option_fromlive(OPTION_LTP, TOKENS_WITHNAMES)
        elif (RESPONSE_DATA['token'] == 41615):
            # If token repeats, close the connection
            print("in appending:elseing")
            I = 0
            close_connection()
            print("best option", best_option_fromlive(OPTION_LTP))
            return best_option_fromlive(OPTION_LTP)
        else:
            print("Please check, Got out of the stream loop::")
            exit()


    # Initialize received_tokens as an empty set

    def on_control_message(wsapp, message):
        logger.info(f"Control Message: {message}")
        # print('LTPLTP:', message['message'])

    def on_open(wsapp):
        logger.info("on open")
        some_error_condition = False
        if some_error_condition:
            error_message = "Simulated error"
            if hasattr(wsapp, 'on_error'):
                wsapp.on_error("Custom Error Type", error_message)
        else:
            sws.subscribe(correlation_id, mode, token_collection)

    def on_error(wsapp, error):
        logger.error(error)

    def on_close(wsapp):
        logger.info("Close")

    def close_connection():
        sws.close_connection()

    # Assign the callbacks.
    sws.on_open = on_open
    sws.on_data = on_data
    sws.on_error = on_error
    sws.on_close = on_close
    sws.on_control_message = on_control_message

    sws.connect()
    I = 0
    close_connection()
    print("Resultant Option for you:", BEST_OPTION)
    return BEST_OPTION



import mysql.connector

def get_valid_options(option_type= False):
    if option_type == False:
        option_type = "CE"
    # Replace with your MySQL database connection details
    db_config = {
        'host': 'localhost',
        'user': 'venu',
        'password': 'venu1515',
        'database': 'mydb'
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare SQL query to retrieve data
        sql_select = "SELECT token, symbol FROM r_inrange_options WHERE validate = %s AND type = %s"
        validate_value = '11SEP24'
        cursor.execute(sql_select, (validate_value, option_type))

        # Fetch all rows
        rows = cursor.fetchall()

        # Create dictionary and list
        result_dict = {token: symbol for token, symbol in rows}
        token_list = [token for token, _ in rows]

        return result_dict, token_list

    except mysql.connector.Error as error:
        print("Error retrieving data from MySQL table:", error)
        return {}, []

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySQL connection is closed")



def ranger_options_tokens(obj):
    i = 11
    options_inrange = ranger_options(obj)
    token_collection = [{}]
    tokens_array = []
    token_name = {}
    token_collection[0]['exchangeType'] = 2
    while i >= 0:
        option_symbol = options_inrange[f'option_' + spell_integer_two(i)]  # Assuming options_inrange is a dictionary
        time.sleep(1)
        searchScriptData = obj.searchScrip("NFO", option_symbol)
        print('for name:',searchScriptData)

        tokens_array.append(searchScriptData['data'][0]['symboltoken'])
        token_name[searchScriptData['data'][0]['symboltoken']] = searchScriptData['data'][0]['tradingsymbol']
        i -= 1
    token_collection[0]['exchangeType'] = 2
    token_collection[0]['tokens'] = tokens_array

    return [token_collection, token_name]


def best_option_fromlive(response_data, forname=False):
    try:
        closest_key = None
        closest_value = None
        closest_shareprice = None

        target_value = 15000

        for item in response_data:
            for key, value in item.items():
                multiplied_value = value * 15
                if multiplied_value <= target_value:
                    if closest_value is None or multiplied_value > closest_value:
                        closest_key = key
                        closest_value = multiplied_value
                        closest_shareprice = value
        if closest_key is not None:
            return {'token': closest_key, 'price': closest_value, 'symbol': forname[closest_key], 'shareprice': closest_shareprice}
        else:
            return None
    except Exception as e:
        print("Error with finding best option: ", e)

def ranger_options(obj, type = 'CE'):

    banknifty_ltp = obj.ltpData("NSE", "BANKNIFTY", 99926009)
    rounded_ltp = banknifty_ltp['data']['ltp'] % 100
    rounded_ltp = round(banknifty_ltp['data']['ltp'] - rounded_ltp)

    i = 0
    range_starts = rounded_ltp - 200
    options_inrange = {}

    while i <= 11:
        symbol_name = "BANKNIFTY"
        validate = "11SEP24"


        options_inrange["option_" + spell_integer_two(i)] = symbol_name + validate + str(range_starts) + type
        range_starts += 100
        i += 1
    options_inrange['current_ltp'] = banknifty_ltp['data']['ltp']
    return options_inrange


#spell integer
def spell_integer_two(n):
    if n < 20:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n]
    if n < 100:
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10-2] + ('_' + spell_integer_two(n%10) if n % 10 else '')
    if n < 1000:
        return spell_integer_two(n//100) + '_hundred_' + spell_integer_two(n%100) if n % 100 else ''
    for i, j in enumerate(('thousand', 'million', 'billion', 'trillion'), 1):
        if n < 1000 ** (i + 1):
            return spell_integer_two(n // 1000 ** i) + '_' + j + '_' + spell_integer_two(n % 1000 ** i) if n % 1000 ** i else ''
    return ''


def get_entered_options():
    try:
        db_config = {
            'host': 'localhost',
            'user': 'venu',
            'password': 'venu1515',
            'database': 'mydb'
        }
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Define the query to fetch records with status "Entered"
        query = "SELECT * FROM r_order_records WHERE status = 'Entered'"
        # Execute the query
        cursor.execute(query)

        # Fetch all the records
        records = cursor.fetchall()
        # Get column names from cursor.description
        column_names = [desc[0] for desc in cursor.description]

        # Convert records to a list of dictionaries
        result = [dict(zip(column_names, record)) for record in records]

        return result

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()