import os
import configparser
from py5paisa import FivePaisaClient
from datetime import datetime
import pandas as pd
import pyotp, time

# Read keys.conf
config = configparser.ConfigParser()
config.read("keys.conf")

app_name = config["KEYS"]["APP_NAME"].strip('"')
app_source = int(config["KEYS"]["APP_SOURCE"])
user_id = config["KEYS"]["USER_ID"].strip('"')
password = config["KEYS"]["PASSWORD"].strip('"')
user_key = config["KEYS"]["USER_KEY"].strip('"')
encryption_key = config["KEYS"]["ENCRYPTION_KEY"].strip('"')

cred = {
    "APP_NAME": app_name,
    "APP_SOURCE": app_source,
    "USER_ID": user_id,
    "PASSWORD": password,
    "USER_KEY": user_key,
    "ENCRYPTION_KEY": encryption_key
}
#--------------------------------------------------------------------------------------
      #SUCCESS CANDLES
      # df=client.historical_data('N','C',1660,'15m','2021-05-25','2021-06-16')

      # req_list_=[{"Exch":"N","ExchType":"D","Symbol":"NIFTY 22 APR 2021 CE 15200.00","Expiry":"20210422","StrikePrice":"15200","OptionType":"CE"}]      
      # feed = client.fetch_market_feed(req_list_)

#--------------------------------------------------------------------------------------
client = FivePaisaClient(cred=cred)

# Replace these with your actual values
client_code = "57266562"
totp = pyotp.TOTP("GU3TENRWGU3DEXZVKBDUWRKZ").now()
pin = "115515"

login = client.get_totp_session(client_code, totp, pin)
req_list_ =  {"Exch": "N", "ExchType": "C", "ScripCode": "2885"}

# df=client.historical_data('N','C',"1660",'15m','2021-05-25','2021-06-16')
# scrips_script = client.get_scrips()
# record = client.query_scrips("N","C","INFY","0","XX","")

scrips = client.get_scrips()
# record = client.query_scrips("N","C","NIFTY","0","XX","")

# print(scrips)
# exit()
print("✅ Logged in via TOTP!")
print(client.get_access_token())

# Login with user credentials
# login_url = "https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey={user_key}&ResponseURL=<Redirect URL>"  # Example, update to correct one

# Perform login
# response = client._login_request(login_url)
# print("Logged in!!" if client.Login_check() else "Login failed.")

# history = client.historical_data('N', 'C', 1660, '15m', '2021-05-25', '2021-06-16')
# print(history)
# # req_list=[
# #             { "Exch":"N","ExchType":"C","ScripCode":1660},
# #             ]

# req_data=client.Request_Feed('mf','s',req_list)
# def on_message(ws, message):
#     print(message)


# client.connect(req_data)

# client.receive_data(on_message)








# # Check login status
# symbol = "RELIANCE"
# exchange = "N"  # N for NSE
# interval = "5m"  # options: 1m, 5m, 15m, 1d, etc.
# start_date = datetime(2024, 3, 1)
# end_date = datetime(2024, 3, 5)

# candles = client.historical_data(
#     exchange=exchange,
#     symbol=symbol,
#     start=start_date,
#     end=end_date,
#     interval=interval
# )

# print(candles.head())
# # print(client.fetch_market_feed_scrip(req_list_))
