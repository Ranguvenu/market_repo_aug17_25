"""
    Created on Monday Feb 2 2022

    @author: Nishant Jain

    :copyright: (c) 2022 by Angel One Limited
"""
import sys
sys.path.append('/var/www/html/market/')  
from SmartApi.smartWebSocketV2 import SmartWebSocketV2

AUTH_TOKEN = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6IlYyODA3NzEiLCJyb2xlcyI6MCwidXNlcnR5cGUiOiJVU0VSIiwidG9rZW4iOiJleUpoYkdjaU9pSklVelV4TWlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKemRXSWlPaUpXTWpnd056Y3hJaXdpWlhod0lqb3hOekEzTmpVd056ZzRMQ0pwWVhRaU9qRTNNRGMxTlRRM05EWXNJbXAwYVNJNkltSTNPRE5pTUdWakxUZGlPV010TkRBNFpDMWlNR0V6TFdJM01HRXpOamRoWXpRM015SXNJbTl0Ym1WdFlXNWhaMlZ5YVdRaU9qUXNJbk52ZFhKalpXbGtJam9pTXlJc0luVnpaWEpmZEhsd1pTSTZJbU5zYVdWdWRDSXNJblJ2YTJWdVgzUjVjR1VpT2lKMGNtRmtaVjloWTJObGMzTmZkRzlyWlc0aUxDSm5iVjlwWkNJNk5Dd2ljMjkxY21ObElqb2lNeUlzSW1SbGRtbGpaVjlwWkNJNklqSTNPVFk0TjJVNExUWXlNV1l0TXpKbE15MDVZakJqTFRBNE9XUTNNRGd6TW1RNU9DSXNJbUZqZENJNmUzMTkua0JyNzdhVm5vZlZnZmIyU0xORVljZTAtU1ZNTU1zOFdQcTBwNTdnRVo3THR6VGVkSFQ0NGZQMDhscVJCOHFUaXRrbWZ2M1JFdE04RGRQRk5hM3NpalEiLCJBUEktS0VZIjoiQ1NoWXFhcEciLCJpYXQiOjE3MDc1NTQ4MDYsImV4cCI6MTcwNzY1MDc4OH0.Gh2PaiyY8c7eoiB6f64l9gK6bQWzCjM9edWIV_7dk0zsHp4RWyUVVLbKskQyH7y7lH1-3JoS1Hn2FqRkd3zjbg'
API_KEY = 'qwert'
CLIENT_CODE = 'V280771'
FEED_TOKEN = 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6IlYyODA3NzEiLCJpYXQiOjE3MDc1NTQ4MDYsImV4cCI6MTcwNzY0MTIwNn0.KGFcErYAbN4QIdoVfFw2Qu9k3E9mOOSqPdFrEoRNcVIcgi79uZtYFEzvgSQg8E9dikvfD-SaJTbtTqJevMwxYg'

correlation_id = "nishant_123_qwerty"
action = 1
mode = 3

token_list = [{"exchangeType": 1, "tokens": ["26009"]}]

sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))


def on_open(wsapp):
    print("on open")
    sws.subscribe(correlation_id, mode, token_list)


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()


