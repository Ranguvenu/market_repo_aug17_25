import sys
sys.path.append('/var/www/html/market/')
# package import statement
# print("scriptdatass")
# exit()
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
from config import *
import pyotp, time
from lib import *
from Symbols import *
from Strategy import *
from datetime import datetime
from mysql.connector import Error
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from orders_lib import *

obj = SmartConnect(api_key="yWjMIfbo")
# 99926000
#login api call

data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
# refreshToken = data['data']['refreshToken']

#-----------------------------------------------------------------------------
# bounds = [50403, 50436, 50720, 50859, 50983, 51175, 51354, 51553, 51828]
# scriptdatass = obj.searchScrip("NFO", "BANKNIFTY24APR2549000CE")

# = {'status': True, 'message': 'SUCCESS', 'errorcode': '', 'data': [{'exchange': 'NFO', 'tradingsymbol': 'BANKNIFTY24APR2551000PE', 'symboltoken': '48003'}]}
# exit()
# orderparams = {'variety': 'NORMAL', 'tradingsymbol': 'BANKNIFTY24APR2552300CE', 'symboltoken': '50948',
#                'transactiontype': 'SELL', 'exchange': 'NFO', 'ordertype': 'MARKET',
#                'producttype': 'CARRYFORWARD', 'duration': 'DAY', 'price': '0', 'squareoff': 0, 'stoploss': 0, 'quantity': 15}
# response = obj.placeOrderFullResponse(orderparams)
# # scriptdata = obj.searchScrip("NFO", "BANKNIFTY24APR2552300CE")
# # print("scriptdata::", scriptdata)
# # print("response::", response)
# # exit()


#-----------------------------------------------------------------------------

live_history_params = {'exchange': 'NSE', 'symboltoken': '99926009', 'interval': 'FIVE_MINUTE', 'fromdate': '2024-05-23 08:10', 'todate': '2024-05-23 09:10'}
# history_date = "2024-05-08 15:25:00"
# current_date = "2024-05-08 15:30:00"
# stream_into_flow(obj,data)
# exit()

try:
    dates = stream_into_flow(obj,data)
except Exception as e:
    print(f"Error is:{(e)}")
    system_notification(f"Error is:{(e)}")
    while True:
        print('Power nap++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        time.sleep(5)
        try:
            dates = stream_into_flow(obj, data)
        except Exception as e:
            time.sleep(5)
            print(f"An error occurred: {e}")
            print("Attempting to reconnect...")
            obj = SmartConnect(api_key="yWjMIfbo")
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
            continue