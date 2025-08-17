import sys
sys.path.append('/var/www/html/market/')
# package import statement
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
from config import *
import pyotp, time
from lib import *
# from live_stream import *
from Symbols import *
from Strategy import *
from datetime import datetime

from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger

# import schedule

#create object of call

obj=SmartConnect(api_key="yWjMIfbo")

#login api call

data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
refreshToken= data['data']['refreshToken']



#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------







history_params = {
     "exchange": "NSE",
     "symboltoken": "99926009",
     "interval": "FIVE_MINUTE",
     "fromdate": "2024-04-15 09:15",
     "todate": "2024-04-15 11:25"
}
params_two = {
    "exchange": "NSE",
    "symboltoken": "99926009",
    "interval": "FIVE_MINUTE",
    "fromdate": "2024-05-07 11:15",
    "todate": "2024-05-07 11:20"
}
history_date = "2024-05-22 15:25:00"
current_date = "2024-05-22 15:30:00"
# stream_into_flow(obj)2024-03-20 12:40:00     2024-02-23 11:20
# dates = flowing_through_history_two(obj, current_date, history_date)
# dates = flowing_through_history_two(obj, current_date, history_date)
# dates = flowing_through_history_two(obj, current_date, history_date)
# exit()
historyhistory = {'exchange': 'NSE', 'symboltoken': '99926009', 'interval': 'FIVE_MINUTE', 'fromdate': '2024-05-22 09:30', 'todate': '2024-05-22 09:30'}

# print(obj.getCandleData(historyhistory))
# exit()

dates = flowing_through_history_two(obj, current_date, history_date)
# exit()
while True:
    try:
        dates = flowing_through_history_two(obj, current_date, history_date)


        history_date = dates['history_date']
        current_date = dates['current_date']
        # exit()
        # stream_into_flow(obj)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Attempting to reconnect...")
        # Reconnect and continue the loop
        
        obj = SmartConnect(api_key="yWjMIfbo")
        history_date = "2024-04-26 09:15:00"
        current_date = "2024-04-26 09:20:00"
        continue# print(obj.getCandleData(params_two))
# exit()
# flowing_through_history(obj)

# history_date = "2024-04-16 15:20:00"
# current_date = "2024-04-16 15:25:00"

#Live stream into the flowing currents
# stream_into_flow(obj)

    


# current_data = {'timestamp_one': '2024-04-16T11:25:00+05:30', 'current_opens': 47541.0, 'highest_price_current': 47547.05, 'lowest_price_current': 47459.7, 'current_closing': 47488.85, 'volume_current': 0, 'current_green': False, 'current_wread': True, 'a_current_opens': 47541.0, 'a_one_opening': 47541.0, 'a_one_closes': 47488.85, 'a_one_closing': 47488.85, 'a_one': 47488.85}




print("the above is history recenting")



#fetch the feedtoken
feedToken=obj.getfeedToken()

data = obj.ltpData(Symbols["Nse"], Symbols["BankNifty"], Symbols["BankNiftyToken"])
try:
    BankNiftyHistory = obj.getCandleData(BankNiftyHistoricParams)
    BankNiftyHistory = BankNiftyHistory["data"]

    # Initializing an empty list to store closing prices
    closing_prices = []

    # Iterating over the data to extract closing prices
    for item in BankNiftyHistory:
        closing_prices.append(item[4])
    # Assuming the response is a JSON object, you can print it or process it further
    print(closing_prices)
except Exception as e:
    # Handle the exception or print an error message
    print(f"Error: {e}")


print('--------------------------------------')


# StreamLTP(Symbols["Nse"], Symbols["BankNifty"],Symbols["BankNiftyToken"], 300, obj)
StreamLTP_two(Symbols["Nse"], Symbols["BankNifty"],Symbols["BankNiftyToken"], 300, obj)
print(StreamLTP_two)

# while True:
#     data = obj.ltpData("NSE", "SBIN-EQ", 3045)
#     current_time_struct = time.localtime()

#     print("Last Trading Price:", data['data']['ltp'], time.strftime("%H:%M:%S", current_time_struct))
#     # schedule.every(5).minutes.do(obj.generateSession('V280771', 4562, pyotp.TOTP(token).now()))

#     time.sleep(10)  # Sleep for 10 seconds before running again
    
print(data)
#place order
# try:
#     orderparams = {
#         "variety": "NORMAL",
#         "tradingsymbol": "SBIN-EQ",
#         "symboltoken": "3045",
#         "transactiontype": "BUY",
#         "exchange": "NSE",
#         "ordertype": "LIMIT",
#         "producttype": "INTRADAY",
#         "duration": "DAY",
#         "price": "555",
#         "squareoff": "0",
#         "stoploss": "0",
#         "quantity": "1"
#         }
#     # orderId=obj.placeOrder(orderparams)
#     print("The order id is: {}".format(orderId))
# except Exception as e:
#     print("Order placement failed: {}".format(e.message))

#gtt rule creation
try:
    gttCreateParams={
            "tradingsymbol" : "SBIN-EQ",
            "symboltoken" : "3045",
            "exchange" : "NSE", 
            "producttype" : "MARGIN",
            "transactiontype" : "BUY",
            "price" : 100000,
            "qty" : 10,
            "disclosedqty": 10,
            "triggerprice" : 200000,
            "timeperiod" : 365
        }
    rule_id=obj.gttCreateRule(gttCreateParams)
    print("The GTT rule id is: {}".format(rule_id))
except Exception as e:
    print("GTT Rule creation failed: {}".format(e.message))
    
#gtt rule list
try:
    status=["FORALL"] #should be a list
    page=1
    count=10
    lists=obj.gttLists(status,page,count)
except Exception as e:
    print("GTT Rule List failed: {}".format(e.message))

#Historic api
try:
    historicParam={
    "exchange": "NSE",
    "symboltoken": "3045",
    "interval": "ONE_MINUTE",
    "fromdate": "2021-02-08 09:00", 
    "todate": "2021-02-08 09:16"
    }
    obj.getCandleData(historicParam)
except Exception as e:
    print("Historic Api failed: {}".format(e.message))
#logout
try:
    logout=obj.terminateSession('V280771')
    print("Logout Successfull")
except Exception as e:
    print("Logout failed: {}".format(e.message))



# ## WebSocket
# from smartapi import WebSocket

# FEED_TOKEN= "your feed token"
# CLIENT_CODE="your client Id"
# token="channel you want the information of" #"nse_cm|2885&nse_cm|1594&nse_cm|11536"
# task="task" #"mw"|"sfi"|"dp"
# ss = WebSocket(FEED_TOKEN, CLIENT_CODE)

# def on_tick(ws, tick):
#     print("Ticks: {}".format(tick))

# def on_connect(ws, response):
#     ws.websocket_connection() # Websocket connection  
#     ws.send_request(token,task) 
    
# def on_close(ws, code, reason):
#     ws.stop()

# # Assign the callbacks.
# ss.on_ticks = on_tick
# ss.on_connect = on_connect
# ss.on_close = on_close

# ss.connect()


