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
history_date = "2025-04-02 14:45:00"
current_date = "2025-04-02 14:50:00"
# dates =

connection_data = connecting_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())

#-----------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------
# print(f"History Date: {history_date}, Current Date: {current_date}")

forword_testing(connecting_object, current_date, history_date, connection_data)
exit()
try:
    dates = forword_testing(connecting_object, current_date, history_date, connection_data)
    history_date = dates['history_date']
    current_date = dates['current_date']

    forword_testing(connecting_object, current_date, history_date, connection_data)
except Exception as e:
    while True:
        print('Power nap++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        time.sleep(5)
        try:
            dates = forword_testing(connecting_object, current_date, history_date, connection_data)

        except Exception as e:
            time.sleep(5)
            print(f"An error occurred: {e}")
            print("Attempting to reconnect...")
            # Reconnect and continue the loop

            obj = SmartConnect(api_key="yWjMIfbo")
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())

            continue