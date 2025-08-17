#Operational Functions
import sys
sys.path.append('/var/www/html/market/')
from SmartApi import SmartConnect
from config import *
from datetime import datetime, timedelta
import pyotp
import time
import pytz
import mysql.connector
from Strategy import *
import smtplib
from email.mime.text import MIMEText
# from live_stream import *
from Symbols import *
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from orders_lib import *
from bear import *
from plyer import notification

#The Connection
# pickup_fromstream()
# exit()
def StreamLTP(Exchange, Symbol, SymbolCode, Intervel, connection):

    # Example: Execute a SELECT query
    # cursor.execute("SELECT * FROM r_ltp_data")
    # result = cursor.fetchall()

    # Example: Insert data into the table


    sample = "sample"
    i = 0
    while True:
        Ltp = connection.ltpData("NSE", "SBIN-EQ", 3045)
        # print('sfdsjfsdf')
        print(Ltp)
        print('goodthings take time')
        # exit()
        Ltp_insertion(i, Ltp)
        current_time_struct = time.localtime()

        # if i == 0:
        #     PriceA = Ltp
        # if PriceA < Ltp and i > 0:
        #     print("Buy")

        # elif PriceA > Ltp and i == 1:
        #     PriceB = Ltp
        # else
        # # print(Ltp)
        # # exit()

        print("Last Trading Price: ", Ltp['data']['ltp'], "@",  time.strftime("%H:%M:%S", current_time_struct))
        time.sleep(Intervel)  # Sleep for "Intervel" seconds before running again
        i += 1


    return sample

def Ltp_insertion(i, Ltp):

    db_config = {
        'host': 'localhost',
        'user': 'venu',
        'password': 'venu1515',
        'database': 'mydb'
    }
    dbconnection = mysql.connector.connect(**db_config)
    cursor = dbconnection.cursor()
    insert_query = "INSERT INTO r_streamed_data (symbol, price, Exchange) VALUES (%s, %s, %s)"
    # print(Ltp)
    # exit()
    data_to_insert = [Ltp['data']['tradingsymbol'], Ltp['data']['ltp'], Ltp['data']['exchange']]
    cursor.execute(insert_query, data_to_insert)

    # Commit the changes to the database
    dbconnection.commit()

def get_records(Table, NumberOfRecentRecords):

    DbConnection = Db_Connection()
    cusrsor = DbConnection.cursor()

    SelectQuery = "SELECT * FROM " + Table + " ORDER BY id DESC LIMIT " + str(NumberOfRecentRecords)
    print(SelectQuery)
    Records = cusrsor.execute(SelectQuery)

    return Records

def Db_Connection():
    db_config = {
        'host': 'localhost',
        'user': 'venu',
        'password': 'venu1515',
        'database': 'mydb'
    }
    return mysql.connector.connect(**db_config)
def round_up_to_nearest_five(x):
    return 5 * ((x + 4) // 5)

def StreamLTP_two(Exchange, Symbol, SymbolCode, Intervel, connection):
    i = 0
    while True:
        Ltp = connection.ltpData(Exchange, Symbol, SymbolCode)
        print(Ltp)
        print('goodthings take time')
        Ltp_insertion(i, Ltp)
        current_time_struct = time.localtime()
        print("Last Trading Price: ", Ltp['data']['ltp'], "@",  time.strftime("%H:%M:%S", current_time_struct))

        # Calculate the time until the next multiple of five minutes
        current_minute = current_time_struct.tm_min
        next_iteration_minute = round_up_to_nearest_five(current_minute)
        minutes_to_sleep = (next_iteration_minute - current_minute) % 60
        if minutes_to_sleep == 0:
            minutes_to_sleep = 5
        print(minutes_to_sleep)
        time.sleep(minutes_to_sleep * 60)  # Sleep until the next multiple of five minutes
        i += 1
def StreamLTP_twotwo(Exchange, Symbol, SymbolCode, Intervel, connection):
    i = 0
    while True:
        Ltp = connection.ltpData(Exchange, Symbol, SymbolCode)
        print(Ltp)
        print('goodthings take time')
        Ltp_insertion(i, Ltp)
        current_time_struct = time.localtime()
        print("Last Trading Price: ", Ltp['data']['ltp'], "@",  time.strftime("%H:%M:%S", current_time_struct))

        # Calculate the time until the next multiple of five minutes
        current_minute = current_time_struct.tm_min
        next_iteration_minute = round_up_to_nearest_five(current_minute)
        minutes_to_sleep = (next_iteration_minute - current_minute) % 60
        if minutes_to_sleep == 0:
            minutes_to_sleep = 5
        print(minutes_to_sleep)
        time.sleep(minutes_to_sleep * 60)  # Sleep until the next multiple of five minutes
        i += 1


def recent_history_forflowing(response_data):
    try:
        formatted_data = {}

        response_data['data'] = list(reversed(response_data['data']))

        i = 1
        for item in response_data['data']:

            timestamp = item[0]
            opening_price = item[1]
            highest_price = item[2]
            lowest_price = item[3]
            closing_price = item[4]
            volume = item[5]  # Assuming this is the volume
            spell = spell_integer(i)

            formatted_data[f'timestamp_{spell}'] = timestamp
            formatted_data[f'opening_price_{spell}'] = opening_price
            formatted_data[f'highest_price_{spell}'] = highest_price
            formatted_data[f'lowest_price_{spell}'] = lowest_price
            formatted_data[f'closing_price_{spell}'] = closing_price
            formatted_data[f'volume_{spell}'] = volume
            formatted_data[f'a_{spell}_green'] = True if closing_price > opening_price else False
            formatted_data[f'a_{spell}_wread'] = True if closing_price < opening_price else False
            formatted_data[f'a_{spell}_opens'] = opening_price
            formatted_data[f'a_{spell}_open'] = opening_price
            formatted_data[f'a_{spell}_opening'] = opening_price
            formatted_data[f'a_{spell}_closes'] = closing_price
            formatted_data[f'a_{spell}_closing'] = closing_price
            formatted_data[f'a_{spell}'] = closing_price
            i += 1


        return formatted_data
    except Exception as e:
        print("Error with (Recent)formating for flowing")
        # Display the formatted data
        # for data_point in formatted_data:
        #     print(data_point)

def current_flowing(response_data):
    try:
        formatted_data = {}

        response_data['data'] = list(reversed(response_data['data']))

        i = 1
        for item in response_data['data']:

            timestamp = item[0]
            opening_price = item[1]
            highest_price = item[2]
            lowest_price = item[3]
            closing_price = item[4]
            volume = item[5]  # Assuming this is the volume

            formatted_data['timestamp_current'] = timestamp
            formatted_data['opening_price_current'] = opening_price
            formatted_data['highest_price_current'] = highest_price
            formatted_data['lowest_price_current'] = lowest_price
            formatted_data['closing_price_current'] = closing_price
            formatted_data['volume_current'] = volume
            formatted_data['current_green'] = True if closing_price > opening_price else False
            formatted_data['current_wread'] = True if closing_price < opening_price else False
            formatted_data['current_opens'] = opening_price
            formatted_data['current_opening'] = opening_price
            formatted_data['current_closes'] = closing_price
            formatted_data['current_closing'] = closing_price
            formatted_data['current'] = closing_price
            i += 1

        return formatted_data

    except Exception as e:
        print("Error with formating the current data for flowing:", e)




#spell integer
def spell_integer(n):
    if n < 20:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n]
    if n < 100:
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10-2] + ('_' + spell_integer(n%10) if n % 10 else '')
    if n < 1000:
        return spell_integer(n//100) + '_hundred_' + spell_integer(n%100) if n % 100 else ''
    for i, j in enumerate(('thousand', 'million', 'billion', 'trillion'), 1):
        if n < 1000 ** (i + 1):
            return spell_integer(n // 1000 ** i) + '_' + j + '_' + spell_integer(n % 1000 ** i) if n % 1000 ** i else ''
    return ''


def recent_number_of_histories_params(exchange, symboltoken, interval, histories_count, candle_timeframe, history_date=False, forlive = False):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    into_past = candle_timeframe * histories_count*60
    if forlive:
        times = recent_historion_timeline(candle_timeframe, into_past, history_date)
    else:
        times = recent_historion_timeline_forlive(candle_timeframe, into_past, history_date)


    # print(times['startime_from_readable'])
    # exit()
    history_params = {
        "exchange": f"{exchange}",
        "symboltoken": f"{symboltoken}",
        "interval": f"{interval}",
        # "fromdate": "2024-04-15 11:15",
        "fromdate": times['startime_to_readable'],
        "todate":times['startime_from_readable']
        # "todate": "2024-04-15 11:25"
    }
    return history_params

def recent_number_of_histories_params_forlive(exchange, symboltoken, interval, histories_count, candle_timeframe, history_date=False, live_history = False):
    try:
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # history_date = False
        into_past = candle_timeframe * histories_count*60
        times = recent_historion_timeline(candle_timeframe, into_past, history_date, live_history)
        # print(times)
        # exit()
        # print(times)
        # exit()
        # if live_history:
        #     print(times)
        #     exit()

        history_params = {
            "exchange": f"{exchange}",
            "symboltoken": f"{symboltoken}",
            "interval": f"{interval}",
            # "fromdate": "2024-04-15 11:15",
            "fromdate": times['startime_to_readable'],
            "todate":times['startime_from_readable']
            # "todate": "2024-04-15 11:25"
        }
        return history_params
    except Exception as e:
        print("Error with history params: ", e)

def recent_number_of_histories_params_two(exchange, symboltoken, interval, histories_count, candle_timeframe):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    into_past = candle_timeframe * histories_count*60
    times = recent_historion_timeline(candle_timeframe, into_past)
    # print(times['startime_from_readable'])
    # exit()
    history_params = {
        "exchange": f"{exchange}",
        "symboltoken": f"{symboltoken}",
        "interval": f"{interval}",
        # "fromdate": "2024-04-15 11:15",
        "fromdate": times['startime_to_readable'],
        "todate":times['startime_from_readable']
        # "todate": "2024-04-15 11:25"
    }
    return history_params


def recent_historion_timeline_forlive(interval = False, into_past=False, current_time=False, forlive_history = False):
    # Get current local time
    # uncomment for live

    # current_time = "2024-04-23 15:30:00"
    if current_time == False:
        local_time = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    # current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

    #the below two lines code is only for last holidays
    # print(current_time)
    # exit()
    # current_time = "2024-04-16 11:25:00"
    # print('datatime doesnt match', current_time)
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    # print('dsssssssssssssss:', current_time)
    # exit()
    # print(type(current_time))
    # exit()
    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        # print(type(current_time))
        # exit()
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60)

        past_time_starts_unix = time_correction - into_past
        time_correction = datetime.fromtimestamp(time_correction)

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")


        startime_readble = time_correction.strftime("%Y-%m-%d %H:%M")


        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')

        time_correction = (time.mktime(unix) - minutes_diff*60 - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60)

        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


    # return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}





def recent_historion_timeline(interval = False, into_past=False, current_time=False, forlive_history = False):
    # Get current local time
    # uncomment for live------------------------------------------------------

    # current_time = "2024-05-14 09:25"
    if current_time == False:
        local_time = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    # current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

    #the below two lines code is only for last holidays
    # print(current_time)
    # exit()
    # current_time = "2024-04-16 11:25:00"
    # print('datatime doesnt match', current_time)
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    # print('dsssssssssssssss:', type(current_time))
    # exit()
    # print(type(current_time))
    # exit()
    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        # print(type(current_time))
        # exit()
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60 -600)

        past_time_starts_unix = time_correction - into_past
        time_correction = datetime.fromtimestamp(time_correction)

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")


        startime_readble = time_correction.strftime("%Y-%m-%d %H:%M")

        past_time_starts_unix_readable = into_yesterday(past_time_starts_unix_readable)
        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')

        time_correction = (time.mktime(unix) - minutes_diff*60 - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60 -600)

        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
        past_time_starts_unix_readable = into_yesterday(past_time_starts_unix_readable)

        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


    # return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


def recent_historion_timeline_two_for_currentpricess(interval = False, into_past=False):
    # Get current local time

    local_time = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    # current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

    #the below two lines code is only for last holidays
    # current_time = "2024-04-16 11:25:00"
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")


    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - minutes_diff*60)
        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")



        startime_readble = current_time.strftime("%Y-%m-%d %H:%M")

        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - minutes_diff*60)
        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


    # return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}



def next_times_giving(begins="2024-04-15 15:25"):

    begins = into_the_yesterday(begins)

    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")

    begins_unix = int(begins_dt_format.timestamp())
    reduced_unix = begins_unix - 5 * 60
    reduced_time = datetime.fromtimestamp(reduced_unix)
    formatted_date = reduced_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date

# To save the result data in file
def save_data(data):
    if data is not None:
        with open('data_two.txt', 'a') as f:  # 'a' to append data to the file
            f.write(str(data) + '\n')
    else:
        print("Data is None, cannot save to file.")



def flowing_through_history(obj, current_date=False, history_starts=False):

    history_date = "2024-04-16 15:20:00"
    current_date = "2024-04-16 15:25:00"
    i = 0
    while True:
        time.sleep(2)  # Sleep for "Intervel" seconds before running again

        history_date = next_times_giving(history_date)

        current_date = next_times_giving(current_date)
        # print("timegiver H:", history_date)
        # print("timegiver C:", current_date)
        # exit()
        params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 10, 5, history_date)
        print("params:",params)
        current_params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_date)
        print("params2:",current_params)
        # obj=SmartConnect(api_key="yWjMIfbo")

        history = obj.getCandleData(params)
        print("historyyyyyyyyy:", history)

        # current_history = obj.getCandleData(current_params)
        try:
            current_history = obj.getCandleData(current_params)
            if current_history['errorCode'] == 'AG8001':
                obj=SmartConnect(api_key="yWjMIfbo")
                #login api call
                data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
                # refreshToken= data['data']['refreshToken']
                current_history = obj.getCandleData(current_params)

        except Exception as e:
            obj=SmartConnect(api_key="yWjMIfbo")
            #login api call
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
            # refreshToken= data['data']['refreshToken']
            current_history = obj.getCandleData(current_params)

        print("the seee---")
        # while True:
        #     times_forhistory =
        Historion = recent_history_forflowing(history)

        current = current_flowing(current_history)

        if not current:
            print("this is current params:", current_params)
            print("this is current:", current)
            print("current_raw:", current_history['errorCode'])


        Historion.update(current)
        flowfilter(Historion)

        save_tofile = flowfilter(Historion)
        # print("type of response:", type(Historion))
        # exit()
        save_data(save_tofile)
        i += 1
        print("after flow"+str(i))
        time.sleep(2)  # Sleep for "Intervel" seconds before running again

def flowing_through_history_two(obj, current_date=False, history_date=False):

    i = 0
    while True:
        time.sleep(1)  # Sleep for "Intervel" seconds before running again

        history_date = next_times_giving(history_date)

        current_date = next_times_giving(current_date)
        try:

            params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 10, 5, history_date)
            current_params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_date)


            # print('pramsasansns:', current_params)
            # print('hihiiihi')
            history = obj.getCandleData(params)

            current_history = obj.getCandleData(current_params)
            # print(current_history)
            # exit()
            # print('cjdnfjdfj22')

            try:
                current_history = obj.getCandleData(current_params)

                # print(current_history)
                # exit()

            except Exception as e:
                print("In exeption: ")
                print('cjdnfjdfj2')

                obj=SmartConnect(api_key="yWjMIfbo")
                #login api call
                data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
                # refreshToken= data['data']['refreshToken']
                print('pramsasansns:', current_params)
                print('object_object',obj.getCandleData(current_params))
                current_history = obj.getCandleData(current_params)
                print('current_history::::::', current_history)
                # continue

            Historion = recent_history_forflowing(history)
            try:
                current = current_flowing(current_history)
            except Exception as e:
                print('the error is:', e)

            if not current:
                print("this is current params:", current_params)
                print("this is current:", current)


            Historion.update(current)
            flowfilter(Historion, current_params['todate'])
            save_tofile = flow_two(Historion, current_params['todate'])

            fourth_flow(Historion, current_params['todate'])
            high_fiveflow(Historion, current_params['todate'])


            save_data(save_tofile)
            i += 1
            print("after flow"+str(i))
            time.sleep(1)  # Sleep for "Intervel" seconds before running again
        except Exception as e:
            return {'history_date': history_date, 'current_date': current_date}
    return {'history_date':history_date, 'current_date':current_date}



def stream_into_flow(connection_obj, connection_data):
    i = 0
    while True:
        # captured_outputs = sys.stdout = sys.stderr = open('data.txt', 'a')

        time.sleep(2)  # Sleep for "Intervel" seconds before running again
        live_history_params = recent_number_of_histories_params_forlive("NSE", "99926009", "FIVE_MINUTE", 12, 5, False, False)

        current_params = recent_number_of_histories_params_forlive("NSE", "99926009", "FIVE_MINUTE", 0, 5, False, True)
        # current_history = obj.getCandleData(current_params)
        try:
            history = connection_obj.getCandleData(live_history_params)
            current_history = connection_obj.getCandleData(current_params)
        except Exception as e:
            print("Not got candles. And the error is:", e)
            history = connection_obj.getCandleData(live_history_params)
            current_history = connection_obj.getCandleData(current_params)


        Historion = recent_history_forflowing(history)
        current = current_flowing(current_history)
        if not current:
            print("this is current params:", current_params)
            print("this is current:", current)

        Historion.update(current)

        flowfilterv = flowfilter(Historion, current_params['todate'], connection_data, connection_obj)
        # print("This is resultant:", flowfilterv)
        # exit()
        flow_twov = flow_two(Historion, current_params['fromdate'], connection_data, connection_obj)

        fourth_flowv = fourth_flow(Historion, current_params['todate'], connection_data, connection_obj)
        high_fiveflowv = high_fiveflow(Historion, current_params['todate'], connection_data, connection_obj)


        bear_onev = bear_one(Historion, current_params['todate'], connection_data, connection_obj)
        bear_twov = bear_two(Historion, current_params['todate'], connection_data, connection_obj)
        bear_threev = bear_three(Historion, current_params['todate'], connection_data, connection_obj)
        bears = [bear_onev, bear_twov, bear_threev]
        bulls = [flowfilterv, flow_twov, fourth_flowv, high_fiveflowv]
        bulls = [item for item in bulls if item is not None]
        bears = [item for item in bears if item is not None]
        print("Bulls:::::", bulls)
        print("Bears:::::", bears)
        try:
            for bear in bears:
                if bear is not None:
                    print("bear of variable:", bear)
                    # bounds =  
                    # Aug22_2 from the chart
                    # bounds = [50916.43, 51023.45, 511740.29, 51245.07, 51329.55, 51450.28, 51553.5]
                    # bounds = [52652.94, 52904.79, 53189.52, 53391.59, 53640.90, 53848.38, 53915.15] #Established on DEC09
                    # bounds = [52652.94, 52904.79, 53055.43, 53189.52, 53327.78, 53582.74, 53746.05, 53891.83] #Established on DEC10

                    # bounds = [50685.94, 51118.79, 51610.43, 52022] #Established on DEC10
                    # bounds = [49833.72, 49653.27, 49225.57, 49060, 48893.47] #Established on DEC10
                    # bounds = [49653.72, 49824, 500002.92, 50220, 50492.47, 50685.65] #Established on DEC10
                    bounds = [50220.11, 50492.33, 50685.65, 51118.08, 51118.08, 51610.42, 52022.38] #Established on MAR26

                    lower_bound = find_lower_bound(bounds, Historion['current_closing'], margin = 25)

                    option_order_response = option_order_record(connection_obj, bear, "BUY", Historion['current_closing'], lower_bound, 'PE')
                    print("option_order_response::", option_order_response)
        except Exception as e:
            print(f"Error from bears:{(e)}")
        try:
            for var in bulls:
                if var is not None:
                    print("var of variable:", var)
                    # bounds = [50916.43, 51023.45, 511740.29, 51245.07, 51329.55, 51450.28, 51553.5]
                    # bounds = [52652.94, 52904.79, 53055.43, 53189.52, 53327.78, 53582.74, 53746.05, 53891.83] #Established on DEC10
                    # bounds = [49833.72, 49653.27, 49225.57, 49060, 48893.47]
                    # bounds = [49653.72, 49824, 500002.92, 50220, 50492.47, 50685.65] #Established on DEC10
                    bounds = [50220.11, 50492.33, 50685.65, 51118.08, 51118.08, 51610.42, 52022.38] #Established on MAR26



                    upper_bound = find_upper_bound(bounds, Historion['current_closing'], margin = 15)

                    option_order_response = option_order_record(connection_obj, var, "BUY", Historion['current_closing'], upper_bound)
                    print("option_order_response::", option_order_response)
                    # exit()
        except Exception as e:
            print(f"Error from bulls:{(e)}")

        entered_options = get_entered_options()
        print("entered_options: ", entered_options)
        if entered_options:
            fast_looping(connection_obj, entered_options)
            next_loop_in = next_fivemloop_inseconds()
            timer(next_loop_in)
            # time.sleep(next_loop_in)
        # save_tofile = flow_two(Historion)
        # next_fivemloop_insecondss = next_fivemloop_inseconds()
        # save_data(save_tofile)
        i += 1
        print("after flow"+str(i))

        # time.sleep(next_fivemloop_inseconds())  # Sleep for "Intervel" seconds before running again
        if entered_options == []:
            if next_fivemloop_inseconds() >= 0:
                next_loop_in = next_fivemloop_inseconds()
                print('Wait for: ', next_loop_in)
                timer(next_loop_in)
                # time.sleep(next_loop_in)  # Sleep for "Intervel" seconds before running again
            elif next_fivemloop_inseconds() <= 0:
                print("For next 5 minutes")
                next_loop_in = next_fivemloop_inseconds() + 300
                timer(next_loop_in)

def next_fivemloop_inseconds():
    # Get the current time
    now = datetime.now()

    # Calculate the next multiple of 5 minutes
    if now.minute % 5 != 0:
        next_minute = (now.minute // 5 + 1) * 5
    else:
        next_minute = now.minute

    # Handle the case where next_minute is 60
    if next_minute == 60:
        next_minute = 0
        next_time = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        next_time = now.replace(minute=next_minute, second=0, microsecond=0)

    # Calculate the time difference in seconds
    next_loop_inseconds = (next_time - now).total_seconds()

    return int(next_loop_inseconds)

def into_the_yesterday(begins="2024-04-15 09:15:00"):
    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")

    # Extract time component from begins_dt_format
    time_component = begins_dt_format.time()

    # Define the target times for comparison
    # target_time_1 = time(9, 15, 0)
    # target_time_2 = time(9, 10, 0)
    target_time_1 = datetime.strptime("09:15:00", "%H:%M:%S")
    target_time_1 = target_time_1.time()
    target_time_2 = datetime.strptime("09:10:00", "%H:%M:%S")
    target_time_2 = target_time_2.time()
    # print(target_time_1.time())
    # exit()

    # If time is exactly 9:15, return yesterday's 15:35
    if time_component == target_time_1:
        # Calculate yesterday's date by subtracting 1 day
        yesterday = begins_dt_format - timedelta(days=1)
        # Create a new datetime object for yesterday's 15:35
        yesterday = datetime(year=yesterday.year, month=yesterday.month, day=yesterday.day, hour=15, minute=30, second=0)

        yesterday = datetime.strftime(yesterday, "%Y-%m-%d %H:%M:%S")
        return yesterday
    # If time is exactly 9:10, return yesterday's 15:30
    elif time_component == target_time_2:
        # Calculate yesterday's date by subtracting 1 day
        yesterday = begins_dt_format - timedelta(days=1)
        # Create a new datetime object for yesterday's 15:30
        yesterday = datetime(year=yesterday.year, month=yesterday.month, day=yesterday.day, hour=15, minute=25, second=0)
        yesterday = datetime.strftime(yesterday, "%Y-%m-%d %H:%M:%S")

        return yesterday
    else:
        return begins  # Return False if neither condition is met



def send_email(subject, body):

    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Gmail's TLS port
    sender_email = 'venucharyrangu@gmail.com'
    receiver_email = 'venu.chary@moodle.com'
    smtp_username = 'venucharyrangu@gmail.com'
    smtp_password = 'dbvb zwju zuvr hgjv'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()




# def ranger_options(obj):

#     banknifty_ltp = obj.ltpData("NSE", "BANKNIFTY", 99926009)
#     rounded_ltp = banknifty_ltp['data']['ltp'] % 100
#     rounded_ltp = round(banknifty_ltp['data']['ltp'] - rounded_ltp)


#     i = 0
#     range_starts = rounded_ltp - 200
#     options_inrange = {}

#     while i <= 11:
#         symbol_name = "BANKNIFTY"
#         validate = "22MAY24"
#         type = 'CE'

#         options_inrange["option_" + spell_integer(i)] = symbol_name + validate + str(range_starts) + type
#         range_starts += 100
#         i += 1
#     options_inrange['current_ltp'] = banknifty_ltp['data']['ltp']
#     return options_inrange


# def ranger_options_tokens(obj):
#     i = 11
#     closest_option = {'symbol': None, 'price': float('inf')}
#     investing_amount = 2555
#     options_inrange = ranger_options(obj)
#     existing_difference = float('inf')
#     token_collection = [{}]
#     tokens_array = []
#     token_name = {}
#     token_collection[0]['exchangeType'] = 2
#     while i >= 0:
#         option_symbol = options_inrange[f'option_' + spell_integer(i)]  # Assuming options_inrange is a dictionary
#         time.sleep(1)
#         searchScriptData = obj.searchScrip("NFO", option_symbol)
#         print('for name:',searchScriptData)
#         # exit()
#         # print(searchScriptData)
#         # exit()
#         tokens_array.append(searchScriptData['data'][0]['symboltoken'])
#         token_name[searchScriptData['data'][0]['symboltoken']] = searchScriptData['data'][0]['tradingsymbol']
#         i -= 1
#     token_collection[0]['exchangeType'] = 2
#     token_collection[0]['tokens'] = tokens_array
#     # print(tokemns)
#     return [token_collection, token_name]



def the_best_option(obj):
    i = 11
    closest_option = {'symbol': None, 'price': float('inf')}
    investing_amount = 2555
    options_inrange = ranger_options(obj)
    existing_difference = float('inf')
    # print("ranged:",options_inrange)
    # exit()
    while i >= 0:
        option_symbol = options_inrange[f'option_' + spell_integer(i)]  # Assuming options_inrange is a dictionary
        time.sleep(1)
        searchScriptData = obj.searchScrip("NFO", option_symbol)
        time.sleep(2)
        option_ltp = obj.ltpData("NFO", option_symbol, searchScriptData['data'][0]['symboltoken'])
        ltp_per_lot = option_ltp['data']['ltp'] * 30

        difference = abs(ltp_per_lot - investing_amount)

        if difference < existing_difference:
            closest_option['price'] = ltp_per_lot
            closest_option['symbol'] = option_symbol
            existing_difference = difference
        # print("ltp_per_lot:", ltp_per_lot)
        # print("difference:", difference)
        # print("ltp:", option_ltp['data']['ltp'])
        # print('test:', ltp_per_lot)

        # exit()
        i -= 1
    return closest_option







def web_stream(data):
    AUTH_TOKEN = data['data']['jwtToken']
    API_KEY = "yWjMIfbo"
    CLIENT_CODE = "V280771"
    FEED_TOKEN = "feedToken"
    correlation_id = "abc123"
    action = 1
    mode = 1
    token_list = [
        {
            "exchangeType": 1,
            "tokens": ["26009"]
        }
    ]

        #retry_strategy=0 for simple retry mechanism
    sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN,max_retry_attempt=2, retry_strategy=0, retry_delay=10, retry_duration=30)
    def on_data(wsapp, message):
        logger.info("Ticks: {}".format(message))
        # close_connection()

    def on_control_message(wsapp, message):
        logger.info(f"Control Message: {message}")

    def on_open(wsapp):
        logger.info("on open")
        some_error_condition = False
        if some_error_condition:
            error_message = "Simulated error"
            if hasattr(wsapp, 'on_error'):
                wsapp.on_error("Custom Error Type", error_message)
        else:
            sws.subscribe(correlation_id, mode, token_list)
            # sws.unsubscribe(correlation_id, mode, token_list1)

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

# def best_option_fromlive(response_data, forname=False):
#     closest_key = None
#     closest_value = float('inf')
#     target_value = 2500

#     for item in response_data:
#         for key, value in item.items():
#             multiplied_value = value * 15
#             if (multiplied_value <= target_value and (target_value - multiplied_value) < target_value - closest_value) or closest_key is None:
#                 closest_key = key
#                 closest_value = multiplied_value

#     return {'token': closest_key, 'price': closest_value, 'symbol': forname[closest_key], 'shareprice': closest_value/15}


def to_buy_option(obj_connection,symbol_name, symbol_token):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol_name,
            "symboltoken": symbol_token,
            "transactiontype": "BUY",
            "exchange": "NFO",
            "ordertype": "MARKET",
            "producttype": "DELIVERY",
            "duration": "DAY",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": "1"
            }
        # Method 1: Place an order and return the order ID
        orderid = obj_connection.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        # Method 2: Place an order and return the full response
        response = obj_connection.placeOrderFullResponse(orderparams)
        logger.info(f"PlaceOrder : {response}")
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")



def riding_completion_price(in_price):
    support_resistance = [55555, 55655, 55755, 55855, 55955, 56155, 56255, 56355, 56455, 56555]
    # if in_price <


def into_yesterday(past_time_starts_unix_readable):
    # Convert the input time string to a datetime object
    past_time = datetime.strptime(past_time_starts_unix_readable, "%Y-%m-%d %H:%M")

    # Define the time range for the comparison
    time_7_15 = past_time.replace(hour=7, minute=15, second=0, microsecond=0)
    time_9_15 = past_time.replace(hour=9, minute=15, second=0, microsecond=0)

    # Check if the given time falls within the specified range
    if time_7_15 <= past_time <= time_9_15:
        # Calculate the difference in minutes between the given time and 09:15
        time_diff_minutes = (time_9_15 - past_time).seconds // 60

        # Get yesterday's date
        yesterday_date = (past_time - timedelta(days=1)).date()

        # Define yesterday's 15:30 benchmark time
        benchmark_time = datetime.combine(yesterday_date, datetime.min.time()).replace(hour=15, minute=30)

        # Calculate the new past time by subtracting the time difference
        new_past_time = benchmark_time - timedelta(minutes=time_diff_minutes)

        return new_past_time.strftime("%Y-%m-%d %H:%M")
    else:
        return past_time_starts_unix_readable



# # Define a global variable to store the response
# RESPONSE_DATA = None
# TOKENS = []
# OPTION_LTP = []
# I = 0
# BEST_OPTION = None
# TOKENS_WITHNAMES = None

# def pickup_fromstream(obj=False, data=False):
#     # print('hihi')
#     # exit()
#     global TOKENS_WITHNAMES
#     if obj == False or data == False:
#         obj = SmartConnect(api_key="yWjMIfbo")
#         # login api call
#         data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
#     # refreshToken = data['data']['refreshToken']

#     AUTH_TOKEN = data['data']['jwtToken']
#     API_KEY = "yWjMIfbo"
#     CLIENT_CODE = "V280771"
#     FEED_TOKEN = data['data']['feedToken']
#     correlation_id = "abc123"
#     action = 1
#     mode = 1
#     ranger_options = ranger_options_tokens(obj)
#     TOKENS_WITHNAMES = ranger_options[1]
#     token_collection = ranger_options[0]

#     # retry_strategy = 0 for simple retry mechanism
#     sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN, max_retry_attempt=0, retry_strategy=0, retry_delay=10, retry_duration=30)

#     # Initialize TOKENS and OPTION_LTP outside the function

#     def on_data(wsapp, message):
#         global RESPONSE_DATA
#         global TOKENS
#         global OPTION_LTP
#         global I
#         global BEST_OPTION

#         logger.info("Ticks: {}".format(message))

#         RESPONSE_DATA = message

#         token = RESPONSE_DATA['token']  # Assuming the key for token is 'token'
#         last_traded_price = RESPONSE_DATA['last_traded_price']  # Assuming the key for last traded price is 'last_traded_price'
#         if RESPONSE_DATA['token'] not in TOKENS:
#             print("in appending:")
#             TOKENS.append(token)
#             OPTION_LTP.append({token: last_traded_price / 100})
#             I += 1
#             if I >= 11:
#                 print('option_ltplist:', OPTION_LTP)
#                 close_connection()
#                 # print("best option", best_option_fromlive(OPTION_LTP))
#                 print('token names:', TOKENS_WITHNAMES)
#                 BEST_OPTION = best_option_fromlive(OPTION_LTP, TOKENS_WITHNAMES)
#         elif (RESPONSE_DATA['token'] == 41615):
#             # If token repeats, close the connection
#             print("in appending:elseing")

#             close_connection()
#             print("best option", best_option_fromlive(OPTION_LTP))
#             return best_option_fromlive(OPTION_LTP)

#     # Initialize received_tokens as an empty set

#     def on_control_message(wsapp, message):
#         logger.info(f"Control Message: {message}")
#         # print('LTPLTP:', message['message'])

#     def on_open(wsapp):
#         logger.info("on open")
#         some_error_condition = False
#         if some_error_condition:
#             error_message = "Simulated error"
#             if hasattr(wsapp, 'on_error'):
#                 wsapp.on_error("Custom Error Type", error_message)
#         else:
#             sws.subscribe(correlation_id, mode, token_collection)

#     def on_error(wsapp, error):
#         logger.error(error)

#     def on_close(wsapp):
#         logger.info("Close")

#     def close_connection():
#         sws.close_connection()

#     # Assign the callbacks.
#     sws.on_open = on_open
#     sws.on_data = on_data
#     sws.on_error = on_error
#     sws.on_close = on_close
#     sws.on_control_message = on_control_message

#     sws.connect()
#     close_connection()

#     return BEST_OPTION


def find_upper_bound(numbers, given_number, margin):
    try:
        for i in range(len(numbers) - 1):
            if numbers[i] < given_number < numbers[i + 1]:
                if (numbers[i + 1] - given_number) >= margin:
                    return numbers[i + 1]
                else:
                    # If the difference is less than the margin, continue checking subsequent numbers
                    for j in range(i + 2, len(numbers)):
                        if (numbers[j] - given_number) >= margin:
                            return numbers[j]
                return None  # No suitable upper_bound found within the margin

        return None  # In case given_number is outside the range of the numbers
    except Exception as e:
        print(f"Error with finding upper bound: {e}")




def find_bounds(numbers, given_number, margin):
    try:
        lower_bound = None
        upper_bound = None

        for i in range(len(numbers) - 1):
            if numbers[i] < given_number < numbers[i + 1]:
                for j in range(i + 2, len(numbers)):
                    if (numbers[j] - given_number) > margin:
                        return numbers[i], numbers[j]
                return numbers[i], None  # In case no suitable upper_bound is found

        return upper_bound
    except Exception as e:
        print(f"Error with finding bounds: ", e)

def find_lower_bound(numbers, given_number, margin):
    try:
        lower_bound = None

        for i in range(len(numbers) - 1, 0, -1):
            if numbers[i] > given_number > numbers[i - 1]:
                for j in range(i - 1, -1, -1):
                    if (given_number - numbers[j]) >= margin:
                        return numbers[j]
                    lower_bound = numbers[j]
                return lower_bound

        # If no number satisfies the conditions, return the smallest number if it's within the margin
        if given_number > numbers[0] and (given_number - numbers[0]) >= margin:
            return numbers[0]

        return lower_bound
    except Exception as e:
        print(f"Error with finding lower bound: ", e)

def fast_looping(connection_object, entered_options):
    conn = mysql.connector.connect(
        host='localhost',
        user='venu',
        password='venu1515',
        database='mydb'
    )
    cursor = conn.cursor()

    # Define the timezone for Asia/Kolkata
    kolkata_timezone = pytz.timezone('Asia/Kolkata')

    # Perform the initial task here
    # Example initial task

    # Get the current time in Asia/Kolkata timezone
    now = datetime.now(kolkata_timezone)

    # Calculate the next multiple of 5 seconds
    next_second = (now.second // 5 + 1) * 5
    if next_second >= 60:
        next_second = 0
        now += timedelta(minutes=1)
    next_time = now.replace(second=next_second, microsecond=0)

    # Wait until the next multiple of 5 seconds
    time_to_sleep = (next_time - datetime.now(kolkata_timezone)).total_seconds()

    float_timer(time_to_sleep)

    # time.sleep(time_to_sleep)

    while True:
        # Get the current time in Asia/Kolkata timezone
        print(f"Task executed at {datetime.now(kolkata_timezone).strftime('%Y-%m-%d %H:%M:%S')}")
        start_time = time.time()

        # Scenarios come here
        try:
            ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            print("current ltp in fast loop: ", ltp)
        except Exception as e:
            print(f"exiting from here while getting ltp {(e)}")
            print('second try for LTP..')
            ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            print(f"LTP by second try is:{(ltp)}")

        try:
            for entered_option in entered_options:
                print("entered option in for:", entered_option)
                print("entered_option['symbol']:", entered_option['symbol'])

                sell_index = entered_option.get('sell_index')
                if sell_index is not None and ltp is not None:
                    if ((sell_index <= ltp) or (sell_index > ltp and (sell_index - ltp) <= 15)) and entered_option['option_type'] == "CE":

                        try:
                            order_response = option_order_record(connection_object, entered_option, 'SELL', ltp)
                            entered_options = get_entered_options()
                            print("its done" + str(order_response))
                            print("its done")
                        except Exception as e:
                            print(f'Please check something is missing..{e}')
                            exit()
                    elif ((sell_index >= ltp) or (sell_index < ltp and (sell_index - ltp) <= 15)) and entered_option['option_type'] == "PE":
                        print('Sell the entered option(' + entered_option['symbol'] + ') please.')
                        # print('Sell the entered option(' + entered_option['symbol'] + ') please.')
                        # print("Test SELL INDEX: ", sell_index)
                        # print("Test LTP:", ltp)
                        # exit()
                        try:
                            order_response = option_order_record(connection_object, entered_option, 'SELL', ltp, None,  "PE")
                            entered_options = get_entered_options()
                            print("its done" + str(order_response))
                            print("its done")
                        except Exception as e:
                            print(f'Please check something is missing..{e}')
                            exit()
                    else:

                        print(' Else elsy...')
                else:
                    print(f"Sell index or ltp is None. sell_index: {sell_index}, ltp: {ltp}")
            print('In fast loop..')
        except Exception as e:
            print(f"exiting from here {(e)}")
            exit()
        print('Hi this is after loop thats you are checking...')
        try:
            end_time = time.time()
            time_defferance = int(end_time - start_time)
            now = datetime.now(kolkata_timezone)
            if time_defferance > 0:
                seconds_time = now.second - time_defferance
            else:
                seconds_time = now.second
        except Exception as e:
            print(f"Please Find me too {(e)}")
            exit()

        # Check if the current time is 5 seconds before a 5-minute mark
        try:
            if (now.minute % 5 == 4 and now.second >= 55) or (now.minute % 5 == 0 and now.second < 5):
                now_without_seconds = now.replace(second=0, microsecond=0)
                unix_timestamp_without_seconds = int(now_without_seconds.timestamp())
                readable_now_without_seconds = now.replace(second=0, microsecond=0)

                query = "SELECT COUNT(*) FROM r_time_storage WHERE time_in_minutes = %s;"
                cursor.execute(query, (unix_timestamp_without_seconds,))
                count = cursor.fetchone()[0]
                exists = count > 0

                if exists:
                    print("Record exists, continuing loop...")
                    continue
                else:
                    print("Exiting the loop and inserting record...")
                    insert_query = "INSERT INTO r_time_storage (time_in_minutes, time_with_seconds, readable_time) VALUES (%s, %s, %s)"
                    values = (unix_timestamp_without_seconds, readable_now_without_seconds, now)
                    cursor.execute(insert_query, values)
                    conn.commit()  # Ensure you commit the transaction
                    break  # Exit the loop after insertion

        except Exception as e:
            print(f"Can you please find me.. {e}")
            exit()
        print(f"Task executed at {now.strftime('%Y-%m-%d %H:%M:%S')}")

        # Add your task logic here

        # Wait for the next 5-second interval
        try:
            next_second = (now.second // 5 + 1) * 5
            if next_second >= 60:
                next_second = 0
                now += timedelta(minutes=1)
            next_time = now.replace(second=next_second, microsecond=0)

            time_to_sleep = (next_time - datetime.now(kolkata_timezone)).total_seconds()
            time.sleep(time_to_sleep)
        except Exception as e:
            print(f"Please find me {(e)}")
            exit()


def timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Time left: {remaining} seconds", end='\r')
        time.sleep(1)
    print("Time's up!")

def float_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds:.1f} seconds", end='\r')
        time.sleep(0.1)
        seconds -= 0.1
    print("Time's up!                             ")

def system_notification(message):
    notification.notify(
        title='Flow Interuptions',
        message=message,
        timeout=10
    )