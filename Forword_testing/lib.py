from datetime import datetime, timedelta
import pyotp
import time
import pytz
import mysql.connector

# Additional imports from your specific modules
from config import *
from Flower_filter import *
from bear import *
from orders_lib import *


def forword_testing(connection_object, current_time, history_time, connection_data):
    # captured_output = sys.stdout = sys.stderr = open('forword_records/libprints.txt', 'a')
    i = 0
    while True:
        time.sleep(1)  # Sleep for "Intervel" seconds before running again

        history_time = next_times_giving(history_time)
        current_time = next_times_giving(current_time)

        # print(f"History Time1: {history_time}, Current Time1: {current_time}")
        try:

            params = recent_number_of_forwording_histories_params("NSE", "99926009", "FIVE_MINUTE", 6, 5, history_time)
            current_params = recent_number_of_forwording_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_time)


            history = connection_object.getCandleData(params)
            # current_history = connection_object.getCandleData(current_params)
            print('history::::::', history) 
            
            try:
                current_history = connection_object.getCandleData(current_params)
                print('current_history::::::', current_history)

            except Exception as e:
                print("In exeption: ")
                print('cjdnfjdfj2')

                connection_object=SmartConnect(api_key="yWjMIfbo")
                #login api callconnection_object
                data = connection_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
                # refreshToken= data['data']['refreshToken']
                print('pramsasansns:', current_params)
                print('object_object',connection_object.getCandleData(current_params))
                current_history = connection_object.getCandleData(current_params)
                print('current_history::::::', current_history)
                # continue
            Historion = recent_history_forflowing(history)
            # print("Historion::::::", Historion)
            try:
                current = current_flowing(current_history)
                # print("current::::::", current)
            except Exception as e:
                print('the error is:')
                print(f"Error while selling: {e}")
                exit()
            if not current:
                print("this is current params:", current_params)
                print("this is current:", current)
            Historion.update(current)
            # print('tegsujbfjbdujbfbdfsdfjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            #Bulls
            flowfilterv = flowfilter(Historion, current_params['todate'], connection_data, connection_object)

            print("flowfilterv::::::", flowfilterv)

            flow_twov = flow_two(Historion, current_params['todate'], connection_data, connection_object)
            fourth_flowv = fourth_flow(Historion, current_params['todate'], connection_data, connection_object)
            high_fiveflowv = high_fiveflow(Historion, current_params['todate'], connection_data, connection_object)

            #Bears
            bear_onev = bear_one(Historion, current_params['todate'], connection_data, connection_object)
            bear_twov = bear_two(Historion, current_params['todate'], connection_data, connection_object)
            bear_threev = bear_three(Historion, current_params['todate'], connection_data, connection_object)

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            bulls = [flowfilterv, flow_twov, fourth_flowv, high_fiveflowv]
            bulls = [item for item in bulls if item is not None]

            bears = [bear_onev, bear_twov, bear_threev]
            bears = [item for item in bears if item is not None]

            print("bears:::::", bears)
            print("Bulls:::::", bulls)
            for bear in bears:
                print("var of Bear:", bear)
                if bear is not None:
                    bounds = [50220.11, 50492.33, 50685.65, 51118.08, 51118.08, 51610.42, 52022.38] #Established on MAR26
                    lower_bound = find_lower_bound(bounds, Historion['current_closing'], margin = 51)

                    option_order_response = option_order_record(connection_object, bear, "BUY", Historion['current_closing'], lower_bound, 'PE')
                    print("option_order_response::", option_order_response)

            for bull in bulls:
                print("var of Bull:", bull)
                if bull is not None:
                    bounds = [50220.11, 50492.33, 50685.65, 51118.08, 51118.08, 51610.42, 52022.38] #Established on MAR26
                    upper_bound = find_upper_bound(bounds, Historion['current_closing'], margin = 55)

                    option_order_response = option_order_record(connection_object, bull, "BUY", Historion['current_closing'], upper_bound, 'PE')
                    print("option_order_response::", option_order_response)
            print('in usual 5 seconds loop')

            time.sleep(5)
            i += 1
            print("after flow"+str(i))


            # Place your main function logic here that runs after the sleep period.
        except Exception as e:
            return {'history_date': history_time, 'current_date': current_time}
    return {'history_date':history_date, 'current_date':current_date}



def speed_cycle_testing(connection_object, current_time, history_time):
    # captured_output = sys.stdout = sys.stderr = open('forword_records/libprints.txt', 'a')
    connection_data = connection_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())


    index_targets = []

    i = 0
    while True:
        time.sleep(1)  # Sleep for "Intervel" seconds before running again
        try:
            ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            try:
                ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            except Exception as e:
                print("In exeption: ")
                print('cjdnfjdfj2')
                connection_object=SmartConnect(api_key="yWjMIfbo")
                #login api callconnection_object
                data = connection_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
                # refreshToken= data['data']['refreshToken']
                ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
                # continue

                ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']

            try:
                ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            except Exception as e:
                print('the error is:', e)


            i += 1
            print("after flow"+str(i))


            # Place your main function logic here that runs after the sleep period.
            print("Main loop is running.")
        except Exception as e:
            return {'history_date': history_time, 'current_date': current_time}
    return {'history_date':history_date, 'current_date':current_date}



def next_fivemloop_inseconds():
    local_time = time.localtime()
    current_time = int(time.strftime("%M", local_time))
    # print(time.strftime("%M", local_time))

    # Sample next_time
    next_time = time.strftime("%Y-%m-%d %H:%M", local_time)

    if current_time % 5 != 0:
        current_time = (current_time // 5 + 1) * 5

    # Split next_time into date and time components
    date_part, time_part = next_time.split()

    # Replace the minute part with current_time
    new_time = time_part[:3] + str(current_time)

    # Reconstruct the modified next_time
    modified_next_time = date_part + ' ' + new_time
    print("Next History time:", modified_next_time)
    modified_next_time = datetime.strptime(modified_next_time, "%Y-%m-%d %H:%M")
    modified_next_time = int(modified_next_time.timestamp())
    now_the_time = time.time()
    now_the_time = int(now_the_time - (now_the_time % 60))
    next_loop_inseconds = modified_next_time - now_the_time
    if next_loop_inseconds <= 0:
        return 0
    return next_loop_inseconds



def next_times_giving(begins="2024-04-15 15:25"):

    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")

    begins_unix = int(begins_dt_format.timestamp())
    reduced_unix = begins_unix + 5 * 60
    reduced_time = datetime.fromtimestamp(reduced_unix)
    formatted_date = reduced_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date



def recent_number_of_forwording_histories_params(exchange, symboltoken, interval, histories_count, candle_timeframe, history_time=False):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    into_past = candle_timeframe * histories_count*60
    times = recent_historion_timeline_forlive(candle_timeframe, into_past, history_time)


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




def recent_historion_timeline_forlive(interval = False, into_past=False, current_time=False, forlive_history=False):
    # Get current local time
    # uncomment for live

    # current_time = "2024-04-23 15:30:00"

    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:

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




def recent_history_forflowing(response_data):
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


def current_flowing(response_data):
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

def ltp_target_checking(obj, index_targets = [500155]):
    # banknifty_ltp = obj.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
    banknifty_ltp = 500155

    for index_target in index_targets:
        index_target
        if index_target <= banknifty_ltp or (index_target - banknifty_ltp) <= 15:
            db_config = {
                'host': 'localhost',
                'user': 'venu',
                'password': 'venu1515',
                'database': 'mydb'
            }
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            select_query = """
            SELECT symbol, orderid, sell_index, nse_index, bought_at, lot_price, status
            FROM order_records
            WHERE status NOT LIKE 'completed' AND sell_index = 500155
            """
            cursor.execute(select_query)
            rows = cursor.fetchall()
            return rows

def fast_looping(connection_object, entered_options, ltp=None):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Venu@5599',
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
    time.sleep(time_to_sleep)
    # print('hi at fast loop')
    # exit()

    while True:
        # Get the current time in Asia/Kolkata timezone
        print(f"Task executed at {datetime.now(kolkata_timezone).strftime('%Y-%m-%d %H:%M:%S')}")
        start_time = time.time()
        #Schenarios comes here
        try:
            if ltp:
                ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            # ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            print("current ltp in fast loop: ", ltp)
        except Exception as e:
            print('second try for LTP..')
            ltp = connection_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
            print(f"exiting from here while getting ltp {(e)}")

        try:
            for entered_option in entered_options:
                print("entered option in for:", entered_option)
                # if entered_option['sell_index']:
                #     print("entered_option['sell_index']", entered_option['sell_index'])
                print("entered_option['symbol']:", entered_option['symbol'])

                sell_index = entered_option.get('sell_index')
                if sell_index is not None and ltp is not None:
                    if (sell_index <= ltp) or (sell_index > ltp and (sell_index - ltp) <= 15):
                        print('Sell the entered option(' + entered_option['symbol'] + ') please.')
                        try:
                            order_response = option_order_record(connection_object, entered_option, 'SELL', ltp)
                            print("its done" + str(order_response))
                            print("its done")
                        except Exception as e:
                            print(f'Please check something is missing..{e}')
                            exit()
                    else:
                        print(' Else elsy...')
                        # exit()
                else:
                    print(f"Sell index or ltp is None. sell_index: {sell_index}, ltp: {ltp}")
            print('In fast loop..')
        except Exception as e:
            print(f"exiting from here {(e)}")
            exit()
        # if
        # initial_task()
        print('Hi this is after loop thats you are cheking...')
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

        # initial_task()

        # Check if the current time is at a 5-minute mark
        try:
            if now.minute % 5 == 0 and seconds_time % 5 == 0:
                now_without_seconds = now.replace(second=0, microsecond=0)
                unix_timestamp_without_seconds = int(now_without_seconds.timestamp())
                readable_now_without_seconds = now.replace(second=0, microsecond=0)

                query = "SELECT COUNT(*) FROM time_storage WHERE time_in_minutes = %s;"
                cursor.execute(query, (unix_timestamp_without_seconds,))
                count = cursor.fetchone()[0]
                exists = count > 0

                if exists:
                    print("Record exists, continuing loop...")
                    continue
                else:
                    print("Exiting the loop and inserting record...")
                    insert_query = "INSERT INTO time_storage (time_in_minutes, time_with_seconds, readable_time) VALUES (%s, %s, %s)"
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
