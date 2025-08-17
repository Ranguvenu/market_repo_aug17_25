from mysql.connector import Error
from logzero import logger
import mysql.connector
from SmartApi import SmartConnect
from SmartApi.smartWebSocketV2 import SmartWebSocketV2


def option_order(obj, order_details, transaction_type="BUY"):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": order_details['symbol'],
            "symboltoken": order_details['token'],
            "transactiontype": transaction_type,
            "exchange": "NFO",
            "ordertype": "LIMIT",
            "producttype": "CARRYFORWARD",
            "duration": "DAY",
            "price": "0",
            "squareoff": 0,
            "stoploss": 0,
            "quantity": 30
            }
        # Method 1: Place an order and return the order ID
        orderid = obj.placeOrder(orderparams)
        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
    except Exception as e:
        print('error'+ e)




def sell_at(current_index_at = 48555):
    support_resistances = [50055.05, 49918.73, 49593.87, 49257.89, 48951.64]
    next_greater = None
    second_next_greater = None

    for resistance in support_resistances:
        if resistance > current_index_at:
            if next_greater is None:
                next_greater = resistance
            else:
                second_next_greater = resistance
                break
    if next_greater is not None and abs(next_greater - current_index_at) <= 55:
        return second_next_greater

    return next_greater

# order_detailss = {}
# order_detailss['symbol'] = "BANKNIFTY26JUN2452000CE"
# order_detailss['token'] = "56100"
def option_order_record(obj, order_details, transaction_type="BUY", current_index=51150, sell_index=15, option_type="CE"):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": order_details['symbol'],
            "symboltoken": order_details['token'],
            "transactiontype": transaction_type,
            "exchange": "NFO",
            "ordertype": "MARKET",
            "producttype": "CARRYFORWARD",
            "duration": "DAY",
            "price": "0",
            "squareoff": 0,
            "stoploss": 0,
            "quantity": 30
        }

        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
        logger.info(f"PlaceOrder : {response['data']['script']}")
        if transaction_type == "SELL":
            # Update records with reference "symbol"
            db_config = {
                'host': 'localhost',
                'user': 'venu',
                'password': 'venu1515',
                'database': 'mydb'
            }

            update_data = (
                response['data']['orderid'],
                current_index,
                30,  # bought_at
                30,  # lot_price
                'Achieved',
                order_details['token'],
                transaction_type,
                order_details['symbol'],
                option_type
            )
            # print(update_data)
            # exit()

            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()

                # Update query
                update_query = """
                UPDATE order_records
                SET sell_orderid = %s, nse_index = %s, bought_at = %s, lot_price = %s, status = %s, token = %s, type = %s
                WHERE symbol = %s AND sell_orderid IS NULL AND option_type = %s
                """

                # Execute the update query
                cursor.execute(update_query, update_data)

                # Commit the changes
                conn.commit()

            except Exception as e:
                logger.error(f"Error: {e}")
                print('error:', e)
            finally:
                cursor.close()
                conn.close()
        else:
            db_config = {
                'host': 'localhost',
                'user': 'venu',
                'password': 'venu1515',
                'database': 'mydb'
            }

            insert_data = (
                response['data']['script'],
                response['data']['orderid'],
                sell_index,
                current_index,
                30,  # bought_at
                30,  # lot_price
                'Entered',
                order_details['token'],
                transaction_type,
                option_type
            )

            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                insert_query = """
                INSERT INTO order_records (symbol, orderid, sell_index, nse_index, bought_at, lot_price, status, token, type, option_type)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, insert_data)
                conn.commit()
            except Exception as e:
                logger.error(f"Error: {e}")
                print('error:', e)
            finally:
                cursor.close()
                conn.close()
    except Exception as e:
        print("orderparams::", orderparams)
        logger.error(f"Error: {e}")
        print('error::', e)
        exit()

