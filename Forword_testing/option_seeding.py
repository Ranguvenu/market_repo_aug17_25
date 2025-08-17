import sys
sys.path.append('/var/www/html/market/')
from SmartApi import SmartConnect
import pyotp, time
from datetime import datetime
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from config import *
from lib import *




connecting_object = SmartConnect(api_key="yWjMIfbo")
# data = connecting_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
history_date = "2024-07-15 09:15:00"
current_date = "2024-07-15 09:20:00"
# dates =
connection_data = connecting_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
#------------------------------------------------------------------------------------

# banknifty_index = connecting_object.ltpData("NSE", "BANKNIFTY","99926009")
# order_details = {'token': '37095', 'price': 2790.0, 'symbol': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}


# orderparams = {
#     "variety": "NORMAL",
#     "tradingsymbol": "BANKNIFTY29MAY2553700CE",
#     "symboltoken": 53792,
#     "transactiontype": "SELL",
#     "exchange": "NFO",
#     "ordertype": "MARKET",
#     "producttype": "CARRYFORWARD",
#     "duration": "DAY",
#     "price": "0",
#     "squareoff": 0,
#     "stoploss": 0,
#     "quantity": 15
# }
# orderid = connecting_object.placeOrder(orderparams)
# response = connecting_object.placeOrderFullResponse(orderparams)
# print(response)
# exit()
# ltp = connecting_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']

def ranger_options(obj, type= "CE"):

    banknifty_ltp = obj.ltpData("NSE", "BANKNIFTY", 99926009)
    rounded_ltp = banknifty_ltp['data']['ltp'] % 100
    rounded_ltp = round(banknifty_ltp['data']['ltp'] - rounded_ltp)


    i = 0
    range_starts = rounded_ltp - 2500
    options_inrange = {}

    while i <= 45:
        symbol_name = "BANKNIFTY"
        validate = "29MAY25"

        options_inrange["option_" + spell_integer_two(i)] = symbol_name + validate + str(range_starts) + type
        range_starts += 100
        i += 1
    options_inrange['current_ltp'] = banknifty_ltp['data']['ltp']
    return options_inrange, validate

def ranger_options_tokens(obj, type="CE"):
    i = 45
    closest_option = {'symbol': None, 'price': float('inf')}
    investing_amount = 2555
    options_inrange, validate  = ranger_options(obj, type)

    existing_difference = float('inf')
    token_collection = [{}]
    tokens_array = []
    token_name = {}
    token_collection[0]['exchangeType'] = 2
    while i >= 0:
        option_symbol = options_inrange[f'option_' + spell_integer_two(i)]
        time.sleep(1)
        try:
            searchScriptData = obj.searchScrip("NFO", option_symbol)
        except Exception as e:
            try:
                searchScriptData = obj.searchScrip("NFO", option_symbol)
            except Exception as e:
                print(f"An error occurred while searching script: {e}________{option_symbol}")
                exit()
        print('for name:',searchScriptData)
        tokens_array.append(searchScriptData['data'][0]['symboltoken'])
        token_name[searchScriptData['data'][0]['symboltoken']] = searchScriptData['data'][0]['tradingsymbol']
        i -= 1
    token_collection[0]['exchangeType'] = 2
    token_collection[0]['tokens'] = tokens_array
    return token_name, validate

import mysql.connector

def option_seeding(data, validate_value, type="CE"):
    db_config = {
        'host': 'localhost',
        'user': 'venu',
        'password': 'venu1515',
        'database': 'mydb'
    }
    # Connect to MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare SQL query with the type column
        sql = "INSERT INTO inrange_options (symbol, token, validate, type) VALUES (%s, %s, %s, %s)"

        # Iterate through data and execute the query
        for token, symbol in data.items():
            cursor.execute(sql, (symbol, token, validate_value, type))

        # Commit changes
        conn.commit()
        print(cursor.rowcount, "record(s) inserted successfully into inrange_options")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

options, validate = ranger_options_tokens(connecting_object, "PE")
print(option_seeding(options, validate, "PE"))
exit()