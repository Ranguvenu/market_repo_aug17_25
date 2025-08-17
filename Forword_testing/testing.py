import time



#This file to retrieve option
def get_option(type):
    db_config = {
        'host': 'localhost',
        'user': 'venu',
        'password': 'venu1515',
        'database': 'mydb'
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    sql_select = "SELECT token, symbol FROM inrange_options WHERE validate = %s AND type = %s"
    validate_value = '29MAY25'
    cursor.execute(sql_select, (validate_value, "PE"))
    rows = cursor.fetchall()
    return [{token: symbol for token, symbol in rows}]

def get_best_option(connecting_object, from_date, to_date,lot, budget, interval):

    options = get_option("PE")

    options = echo_suitable_options(connecting_object, budget, options, lot)

    """
    Finds the best option from a list based on sensitivity (price change percentage)
    and OI change percentage over a given time window while respecting a rate limit 
    of 1 request per second.
    Parameters:
        options (list): List of dictionaries in the format [{symboltoken: current_price}, ...]
        connecting_object: An object that provides the API functions getCandleData and getOIData.
        from_date (str): Start time in "YYYY-MM-DD HH:MM" format.
        to_date (str): End time in "YYYY-MM-DD HH:MM" format.
        interval (str): Candle/oi interval (default "FIVE_MINUTE").
    Returns:
        dict: Dictionary containing details of the best option.
              Example:
              {
                  "symboltoken": "74970",
                  "current_price": 931.4,
                  "price_change_percent": 55.0,
                  "oi_change_percent": 2.5
              }
    """

    best_option = None
    best_metric = -float("inf")

    for option_dict in options:

        for symboltoken, symboname in option_dict.items():

            params = {
                "exchange": "NFO",
                "symboltoken": symboltoken,
                "interval": interval,
                "fromdate": from_date,
                "todate": to_date
            }
            #-----------------------------------------------------------------------------------------------------------

            try:
                candle_response = connecting_object.getCandleData(params)
                banknifty_ltp = connecting_object.ltpData("NFO", symboname, symboltoken)
            except Exception as e:
                print(f"Error occurred while fetching candle data: {e}")
            #-----------------------------------------------------------------------------------------------------------

            if(banknifty_ltp['data']['ltp']*30 > 7200):
                time.sleep(1)
                continue

            if not candle_response.get("status") or not candle_response.get("data"):
                continue
            candle_data = candle_response["data"]
            if len(candle_data) < 1:
                continue
            open_price = candle_data[0][1]
            close_price = candle_data[-1][4]
            price_change_percent = ((close_price - open_price) / open_price) * 100
            oi_response = connecting_object.getOIData(params)
            time.sleep(1)
            if not oi_response.get("status") or not oi_response.get("data"):
                oi_change_percent = 0
            else:
                oi_data = oi_response["data"]
                if len(oi_data) < 1:
                    oi_change_percent = 0
                else:
                    initial_oi = oi_data[0]["oi"]
                    final_oi = oi_data[-1]["oi"]
                    oi_change_percent = ((final_oi - initial_oi) / initial_oi) * 100 if initial_oi != 0 else 0
            combined_metric = price_change_percent 
            if combined_metric > best_metric:
                best_metric = combined_metric
                best_option = {
                    "token": symboltoken,
                    "symbol": symboname,
                    "price": price_change_percent,
                    "shareprice": oi_change_percent
                }
    return best_option

options = [{
  "75118": "BANKNIFTY29MAY2554100CE",
  "75044": "BANKNIFTY29MAY2554000CE",
  "75020": "BANKNIFTY29MAY2553900CE",
  "75016": "BANKNIFTY29MAY2553800CE",
  "75014": "BANKNIFTY29MAY2553700CE",
  "75012": "BANKNIFTY29MAY2553600CE",
  "75010": "BANKNIFTY29MAY2553500CE",
  "75008": "BANKNIFTY29MAY2553400CE",
  "75006": "BANKNIFTY29MAY2553300CE",
  "75004": "BANKNIFTY29MAY2553200CE",
  "75002": "BANKNIFTY29MAY2553100CE",
  "75000": "BANKNIFTY29MAY2553000CE",
  "74998": "BANKNIFTY29MAY2552900CE",
  "74996": "BANKNIFTY29MAY2552800CE",
  "74994": "BANKNIFTY29MAY2552700CE",
  "74992": "BANKNIFTY29MAY2552600CE",
  "74990": "BANKNIFTY29MAY2552500CE",
  "74988": "BANKNIFTY29MAY2552400CE",
  "74986": "BANKNIFTY29MAY2552300CE",
  "74984": "BANKNIFTY29MAY2552200CE",
  "74982": "BANKNIFTY29MAY2552100CE",
  "74980": "BANKNIFTY29MAY2552000CE",
  "74978": "BANKNIFTY29MAY2551900CE",
  "74976": "BANKNIFTY29MAY2551800CE",
  "74974": "BANKNIFTY29MAY2551700CE",
  "74972": "BANKNIFTY29MAY2551600CE",
  "74970": "BANKNIFTY29MAY2551500CE",
  "74968": "BANKNIFTY29MAY2551400CE",
  "74966": "BANKNIFTY29MAY2551300CE",
  "74964": "BANKNIFTY29MAY2551200CE",
  "74962": "BANKNIFTY29MAY2551100CE",
  "74891": "BANKNIFTY29MAY2551000CE",
  "74885": "BANKNIFTY29MAY2550900CE",
  "74863": "BANKNIFTY29MAY2550800CE",
  "74829": "BANKNIFTY29MAY2550700CE",
  "74824": "BANKNIFTY29MAY2550600CE",
  "74822": "BANKNIFTY29MAY2550500CE",
  "74818": "BANKNIFTY29MAY2550400CE",
  "74814": "BANKNIFTY29MAY2550300CE",
  "74812": "BANKNIFTY29MAY2550200CE",
  "74810": "BANKNIFTY29MAY2550100CE",
  "74808": "BANKNIFTY29MAY2550000CE",
  "74806": "BANKNIFTY29MAY2549900CE",
  "74802": "BANKNIFTY29MAY2549800CE",
  "74800": "BANKNIFTY29MAY2549700CE",
  "74779": "BANKNIFTY29MAY2549600CE",
  "74768": "BANKNIFTY29MAY2549500CE",
  "74757": "BANKNIFTY29MAY2549400CE",
  "74739": "BANKNIFTY29MAY2549300CE",
  "74733": "BANKNIFTY29MAY2549200CE",
  "74729": "BANKNIFTY29MAY2549100CE",
  "74727": "BANKNIFTY29MAY2549000CE"
}]
def echo_suitable_options(connecting_object, limit, options, lot):
    suitables = {}
    for token, symbol in options[0].items():
        import time

        max_retries = 10 
        retry_delay = 1
        attempt = 0
        ltp = None

        while ltp is None and attempt < max_retries:
            try:
                ltp = connecting_object.ltpData("NFO", symbol, token)
                print(f"✅ LTP for {symbol} is {ltp}")
            except Exception as e:
                attempt += 1
                print(f"⚠️ Attempt {attempt}: Failed to retrieve LTP for {symbol} (Token: {token}) - {e}")
                time.sleep(retry_delay)

        if ltp is None:
            print(f"❌ Could not retrieve LTP for {symbol} after {max_retries} attempts.")
        #-------------------------------------------------------------------------------------------------
        if ltp['data']['ltp']*lot <= limit:
            suitables[token] = symbol
    return [suitables]

best_option = get_best_option(connecting_object, "2025-05-15 09:15", "2025-05-15 14:15",30, 10000,"FIVE_MINUTE")
print("best_option::", best_option)
exit()
