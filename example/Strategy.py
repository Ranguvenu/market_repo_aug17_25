import pandas as pd
import sys
from db import *
from optionslib import *

# from live_stream import *
# pickup_fromstream('connection_obj', 'connection_data')
# exit()
#x1 is Least recent closing price and x5 is most recent closing price and y1 current price
def strategy(x1, x2, x3, x4, x5, y1):
    if x1 > x2 > x3 < x4 < x1 < x5 and y1 > x1:
        print('ample text: Bull')




def check_buy_signal(current_price, recent_closing_prices, support_resistance_price):
    """
    Checks if the current price generates a buy signal based on the described strategy.

    Parameters:
    - current_price: Current price of the stock.
    - recent_closing_prices: List of the most recent 10 closing prices of the stock.
    - support_resistance_price: Static support/resistance price for the stock.

    Returns:
    - True if a buy signal is generated, False otherwise.
    """

    # Ensure we have at least 10 closing prices
    if len(recent_closing_prices) < 10:
        print("Need Least 10 Closing Prices")
        return False

    # Identify green candles (closing price higher than the open price)
    green_candles = [price for price in recent_closing_prices if price > 0]

    # Check if there are at least 2 green candles
    if len(green_candles) < 2:
        return False

    # Create a DataFrame with 'close' column using only green candles
    data = pd.DataFrame({'close': green_candles})

    # Initialize variables
    window_size = 2  # Number of candles to check for sideways movement
    fluctuation_threshold = 0.002  # 0.2% fluctuation threshold
    move_down_threshold = 0.002  # 0.2% move down threshold

    # Extract relevant window of data
    window_data = data.head(window_size)

    # Calculate price fluctuations in the window
    price_fluctuations = window_data['close'].pct_change()

    # Check if the stock moves sideways with fluctuation under 0.2%
    if all(abs(fluctuation) < fluctuation_threshold for fluctuation in price_fluctuations):
        # Check if the stock comes down about 0.4%
        if price_fluctuations.sum() < -move_down_threshold:
            # Find the highest closing price in the window
            highest_closing_price = window_data['close'].max()

            # Check if the stock comes back and crosses the highest closing price near the support/resistance level
            if current_price > highest_closing_price and current_price > support_resistance_price:
                # Buy signal identified
                return True

    return False


def SupportResistance(BeginsAt, EndsAt):
    records = []

    SupportResistance = BeginsAt

    while SupportResistance <= EndsAt:
        records.append(round(SupportResistance, 3))
        #Support/Resistance for every 0.5% of priveous support/Resistance
        SupportResistance = SupportResistance * 1.005
    return records


# def checkcolor():
    # save the record in db with "status" is green or wread
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


def flowfilter(payload, timeofcalling, connection_data=False, connection_obj=False):
#     if connection_data:
#         captured_output = sys.stdout = sys.stderr = open('alive/datafilsterflow.txt', 'a')
#     else:
        # captured_output = sys.stdout = sys.stderr = open('datafilsterflow.txt', 'a')

    # print("flow_one_three_three_two")
    # print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>testing")
    # if connection_data:

    #     resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
    #     print("Resultant option:", resultant_option)

    #     return resultant_option
    # if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
    #     print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmedtesting")
    #     greenery_recording(payload['current_closing'], timeofcalling, True, 'one')
    # else:
    #     greenery_recording(payload['current_closing'], timeofcalling, False, 'one')
    # exit()
    i = 1
    print("This is current closing:",payload['current_closing'])
    print("Testing at:", timeofcalling)

    try:
        if payload['current_green'] and payload['current_closing'] > payload['a_one']and payload['a_one_green'] and payload['a_one']> payload['a_two']and payload['a_two_green']:
            print('in stage')

            #flow_one-stage-one
            if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_two']and payload['a_three_opens'] < payload['a_one']:
                print("flow_one_one")

            if payload['a_three_wread'] and payload['a_three_opens'] > payload['current_closing']:
                print("flow_one_two")

            if  payload['a_three_wread'] and payload['a_three_opens'] > payload['a_one']and payload['a_three_opens'] < payload['current_closing'] and payload['a_three_opens'] > payload['a_one_closes']:
                print("flow_one_three")
            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four")

            if payload['a_three_wread'] and payload['a_three_opens'] < payload['a_two_closes']:
                print("flow_one_five")

            # flow_one-stage-one
            if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_two'] and payload['a_three_opens'] < payload['a_one']:
                print("flow_one_one copied")
                if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closing']:
                    print("flow_one_one_one --- stage_three_started")
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                    print("flow_one_one_two --- stage_three")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closing']:
                    print("flow_one_one_three --- stage_three")
                if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_one_closing'] and payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_one_four --- stage_three")
                if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                    print("flow_one_one_five --- stage_three It's out of first flow")
                if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                    print("flow_one_one_six --- stage_three")

                if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                    print("flow_one_one_six --- stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_one_six_one ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_one_six_two ---- stage_four")
                    if payload['a_five_wread'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_one_one_six_three ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                        print("flow_one_one_six_four ---- stage_four")
                    if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                        print("flow_one_one_six_five ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_one_six_six ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_one_six_seven ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_one_six_eight ---- stage_four")

                # stage four in stage three
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                    print("flow_one_one_two --- stage_three copied")

                    if payload['a_five_green']:
                        print("flow_one_one_two_one --- stage_four_started")

                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_one_two_two --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_one_two_three --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_one_two_four --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_one_two_five --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_one_two_six --- stage_four")

                if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_one_closing'] and payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_one_four --- stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_one_four_one ---- stage_four_started")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_one_four_two ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_one_four_three ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_one_one_four_four ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing'] and payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_one_four_five ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_one_four_six ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_one_four_seven ---- stage_four")



                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closing']:
                    print("flow_one_one_three --- stage_three")

                    # if a_five_wread and a_five_opens >
            #---------------------------------------------------------------------------

                #flow_one_four    --stage_two

            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four copied")
                if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                    print("flow_one_four_one It's out of first flow")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closes']:
                    print("flow_one_four_two")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_two_closes'] and payload['a_four_opens'] > payload['a_three_closes']:
                    print("flow_one_four_three")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closes'] and payload['a_four_opens'] > payload['a_two_closes']:
                    print("flow_one_four_four")

                if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_one_closes'] and payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_four_five  --------- signal might come from here")

                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_opens'] and payload['a_four_closing'] < payload['a_three_closes']:
                    print("flow_one_four_six Verified")


            if payload['a_three_wread'] and payload['a_three_opens'] < payload['a_two_closes']:
                print("flow_one_five")

                if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closing']:
                    print("flow_one_five_one --- stage_three_started")
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                    print("flow_one_five_two --- stage_three")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_two_closing']:
                    print("flow_one_five_three --- stage_three")
                if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing'] and payload['a_four_opens'] < payload['a_one_closing']:
                    print("flow_one_five_four --- stage_three")
                if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_five_five --- stage_three")
                if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                    print("flow_one_five_six --- stage_three")


                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                    print("flow_one_five_two --- stage_three")

                    if payload['a_five_green']:
                        print("flow_one_five_two_one --- stage_four Verified")
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_five_two_two --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_two_closing']:
                        print("flow_one_five_two_three --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_five_two_four --- stage_four")
                    if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                        print("flow_one_five_two_five --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_five_two_six --- stage_four")

                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_two_closing']:
                    print("flow_one_five_three --- stage_three")

                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_five_three_one --- stage_four_started")
                    if payload['a_five_green'] and payload['a_four_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_five_three_two --- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_five_three_three --- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_five_three_four --- stage_four")
                    if payload['a_five_wread'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_five_three_five --- stage_four")
                    if payload['a_five_wread'] and payload['current_closing'] > payload['a_two_closing'] > payload['a_one_closing']:
                        print("flow_one_five_three_six --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_five_three_seven --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                        print("flow_one_five_three_eight --- stage_four")

                if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing'] and payload['a_four_opens'] < payload['a_one_closing']:
                    print("flow_one_five_four --- stage_three")

                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_five_four_one ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_one_five_four_two --- stage_four")
                    if payload['a_five_green'] and payload['a_four_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_five_four_three --- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_five_four_four --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_five_four_five --- stage_four")
                    if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                        print("flow_one_five_four_six --- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_five_four_seven --- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_five_four_eight --- stage_four")

                if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_five_five --- stage_three")

                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_five_five_one ---- stage_four")
                    if payload['a_five_green'] and payload['a_three_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_five_five_two ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_five_five_three ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_five_five_four ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_five_five_five ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_five_five_six ---- stage_four")



            #---------------------------------------------------------------------------

                    #flow_one_three   --stage_two

            if  payload['a_three_wread'] and payload['a_three_opens'] > payload['a_one']and payload['a_three_opens'] < payload['current_closing'] and payload['a_three_opens'] > payload['a_one_closes']:
                print("flow_one_three ------copied")
                #in pratice it not possible to "a_four_opens == a_three_closes", make it aprox
                if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closes']:
                    print("flow_one_three_one")

                if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                    print("flow_one_three_two")
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closes']:
                    print("flow_one_three_three")
                if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closes']:
                    print("flow_one_three_four")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_three_five")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_three_five")

            #--------------------------------------------------------------------------------------------

                #flow_one_three_one   --stage_three


            #in pratice it not possible to "a_four_opens == a_three_closes", make it aprox
                if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closes']:
                    print("flow_one_three_one ---copied")

                    if payload['a_five_green']:
                        print("flow_one_three_one_one  --signal is here (2nd degree)")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_three_one_two --signal is here (2nd degree)")
                        #In practice it is almost not possible, Please make it approx
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_three_one_three -- might become the signal(3rd degree)")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_one_three_one_four")


            #------------------------------------------------------------------------------------------------

                #flow_one_three_three   --stage_three
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closes']:
                    print("flow_one_three_three --copied")

                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_opens']:
                        print("flow_one_three_three_one")
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                            greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_three_one")
                        else:
                            greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_three_one")
                        if connection_data:
                            resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                            print("Resultant option:", resultant_option)
                            return resultant_option


                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_three_three_two")
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                            greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_three_two")
                        else:
                            greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_three_two")
                        if connection_data:
                            resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                            print("Resultant option:", resultant_option)
                            return resultant_option

                    #in pratice it not possible to "a_five_opens == a_four_closing", make it aprox
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_three_three_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_three_three_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_three_three_five")

            #---------------------------------------------------------------------------------------------------------------

                    # flow_one_three_four --stage_three
                    if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closes']:
                        print("flow_one_three_four  ---copied")

                        if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closes']:
                            print("flow_one_three_four_one")
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                                greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_four_one")
                            else:
                                greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_four_one")
                            if connection_data:
                                resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                                print("Resultant option:", resultant_option)
                                return resultant_option


                        if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closes']:
                            print("flow_one_three_four_two")
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                                greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_four_two")
                            else:
                                greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_four_two")
                            if connection_data:
                                resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                                print("Resultant option:", resultant_option)
                                return resultant_option

                        if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                            print("flow_one_three_four_three")
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                                greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_four_three")
                            else:
                                greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_four_three")
                            if connection_data:
                                resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                                print("Resultant option:", resultant_option)
                                return resultant_option

                        # in practice it's not possible to "a_five_opens == a_four_closing", make it approximate
                        if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                            print("flow_one_three_four_four")
                        if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                            print("flow_one_three_four_five")
                        if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] > payload['current_closing']:
                            print("flow_one_three_four_six")
                    # ----------------------------------------------------------------------------------------------------------------

                    # flow_one_three_five --stage_three
                    if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                        print("flow_one_three_five ---copied")

                        if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                            print("flow_one_three_five_one")
                        if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing'] and payload['a_five_opens'] > payload['a_three_closes']:
                            print("flow_one_three_five_two")
                        if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing'] and payload['a_five_opens'] < payload['a_three_closes']:
                            print("flow_one_three_five_three")
                        if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_five_opens'] and payload['a_five_opens'] < payload['current_closing']:
                            print("flow_one_three_five_four")
                        if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                            print("flow_one_three_five_five ")

                #flow_one_four    --stage_two
            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four copied two")

                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closes']:
                    print("flow_one_four_two --stage_two_for_stage_three copies")
                    if payload['a_five_green'] and payload['a_five_closing'] == payload['a_four_opens']:
                        print("flow_one_four_two_one --stage_three_started")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_four_two_two --stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_four_two_three --stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['a_two_closing']:
                        print("flow_one_four_two_four --stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_four_two_five --stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_four_two_six --stage_three")
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_two_seven --stage_three It's out of first flow")

            # flow_one_four    --stage_two
            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four copied two")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_two_closes'] and payload['a_four_opens'] > payload['a_three_closes']:
                    print("flow_one_four_three stage_two_for_stage_three copied")

                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_four_three_one ---stage_three_started")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_four_three_two ---stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                        print("flow_one_four_three_three ---stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_four_three_four ---stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_four_three_five ---stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_three_six ---stage_three It's out of first flow")


            # flow_one_four    --stage_two
            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four copied two")
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closes'] and payload['a_four_opens'] > payload['a_two_closes']:
                    print("flow_one_four_four stage_two_for_stage_three copied")

                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_four_four_one stage_three_started")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_four_four_two stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_four_four_three stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_four_four stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_four_five stage_three It's out of first flow")


            # flow_one_four    --stage_two
            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four copied two")
                if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_one_closes'] and payload['a_four_opens'] < payload['current_closing']:
                    print("flow_one_four_five  ---------  stage_two_starts_for_stage_three signal might come from here copied")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_five_one ---stage_three_started")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_four_five_two ---stage_three")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_four_five_three ---stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_five_four ---stage_three")

            # flow_one_four    --stage_two
            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_opens'] and payload['a_three_closes'] < payload['a_two_closes']:
                print("flow_one_four copied two")
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_opens'] and payload['a_four_closing'] < payload['a_three_closes']:
                    print("flow_one_four_six stage_two_starts_stage_three copied")
                    if payload['a_five_green']:
                        print("flow_one_four_six_one stage_three_started Verified")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_four_six_two stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print('flow_one_four_six_three stage_three')
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['a_two_closing']:
                        print("flow_one_four_six_four stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing'] and payload['a_five_opens'] < payload['a_one_closing']:
                        print("flow_one_four_six_five stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_four_six_six stage_three")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_four_six_seven stage_three")



            if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_one'] and payload['a_three_opens'] < payload['current_closing'] and payload['a_three_opens'] > payload['a_one_closes']:
                print("flow_one_three copied")
                if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closes']:
                    print("flow_one_three_three copied")
                    if payload['a_five_green']:
                        print("flow_one_three_three_one stage_four_started")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_three_three_two ----stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_three_three_three ----stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_three_three_four ----stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_three_three_five ----stage_four It's out of first flow")

            if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_one'] and payload['a_three_opens'] < payload['current_closing'] and payload['a_three_opens'] > payload['a_one_closes']:
                print("flow_one_three copied")
                if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closes']:
                    print("flow_one_three_four copied")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_three_four_one stage_four_started")
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")

                        if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                            greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_four_one stage_four")
                        else:
                            greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_four_one stage_four")
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_three_four_two stage_four")
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")

                        if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                            greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_four_two")
                        else:
                            greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_four_two")
                        if connection_data:
                            resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                            print("Resultant option:", resultant_option)
                            return resultant_option


                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_one_three_four_three stage_four")
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                            print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                            greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "flow_one_three_four_three")
                        else:
                            greenery_recording(payload['current_closing'], timeofcalling, False, 'one', "flow_one_three_four_three")
                        if connection_data:
                            resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                            print("Resultant option:", resultant_option)
                            return resultant_option


                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_one_three_four_four stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_three_four_five stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_three_four_six stage_four")

            if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_one'] and payload['a_three_opens'] < payload['current_closing'] and payload['a_three_opens'] > payload['a_one_closes']:
                print("flow_one_three copied")
                if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closes']:
                    print("flow_one_three_four copied for_stage_four")

                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_one_three_four_one stage_four_started")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing'] and payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_one_three_four_two stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_one_three_four_three stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_one_three_four_four stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_one_three_four_five stage_four")



        else:
            print("its out of flow9stage")
            # exit()
        # # flow_one -stage_one
    except Exception as e:
        print(f"First flow strategic error:{(e)}")























def flow_two(payload, weareat=False, connection_data=False, connection_obj=False):
    # if connection_data:
        # captured_output = sys.stdout = sys.stderr = open('alive/dataflowtwo.txt', 'a')
    # else:
        # captured_output = sys.stdout = sys.stderr = open('dataflowtwo.txt', 'a')


    print("Now we are at:", weareat)
    print("Second flow has been called. now the current is:", payload['current_closing'])

    # # flow_one -stage_one

    if payload['current_green'] and payload['a_one_green'] and payload['a_two_wread'] and payload['a_two_opens'] > payload['a_one_closing'] and payload['a_two_opens'] < payload['current_closing']:

        print("flow_two -stage_one")
        # exit()
        # flow_two_one --stage-two-start

        if payload['a_three_wread'] and payload['a_three_opens'] < payload['current_closing']:
            print("flow_two_one --stage_two")
        # flow_two_two --stage_two
        if payload['a_three_wread'] and payload['a_three_opens'] > payload['current_closing']:
            print("flow_two_two --stage_two falsy")
        # flow_two_three --stage_two

        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three")
        # flow_two_four --stage_two
        if payload['a_three_green'] and payload['a_three_opens'] == payload['a_two_closing']:
            print("flow_two_four")
        # flow_two_five --stage_two
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_two")

        # flow_two_one ---stage_three-starts
        if payload['a_three_wread'] and payload['a_three_opens'] < payload['current_closing']:
            print("flow_two_one --stage_two -copied")
            # flow_two_one_one ---stage_three-starts

            #                  approx
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_one_one ---stage_three")
            # flow_two_one_two ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_two_one_two ---stage_three")
            # flow_two_one_three ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_two_one_three --- stage_three")
            # flow_two_one_four ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_two_closing']:
                print("flow_two_one_four ---stage_three")
            # flow_two_one_five ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_one_five ---stage_three")
            # flow_two_one_six ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_two_one_six ---stage_three")




            # Stage four in stage three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_two_one_two --- stage_three copied")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_two_one_two_one --- stage_four_started")

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_one_two_two --- stage_four")

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_two_one_two_three --- stage_four")

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print('flow_two_one_two_four --- stage_four')


                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_one_two_five --- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_one_two_six --- stage_four")


                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_one_two_seven --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_one_two_eight --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_one_two_nine --- stage_four")



                
            # Stage four in stage three
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_two_one_three --- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_one_three_one --- stage_four_started")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_one_three_one")
                    else:
                        greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_one_three_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_two_one_three_two --- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_one_three_two")
                    else:
                        greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_one_three_two")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_two_one_three_three --- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_one_three_three")
                    else:
                        greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_one_three_three")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_one_three_four --- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_one_three_five --- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_one_three_six --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_one_three_seven --- stage_four Verified")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_one_three_seven")
                    else:
                        greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_one_three_seven")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option





            # flow_two_one_five --- stage_three
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_one_five --- stage_three")
                # print('and this our payload:', payload)
                # exit()
                if payload['a_five_green'] and payload['a_five_opens']:
                    print("flow_two_one_five_one ---- stage_four_started")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_one_five_one")
                    else:
                        greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_one_five_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_one_five_two ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_one_five_two")
                    else:
                        greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_one_five_two")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_one_five_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_one_five_four ---- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_one_five_five ---- stage_four")



        # flow_two_three ---stage_three -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_three_starts -copied")
            # flow_two_three_one ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_two_three_one ---stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_three_one")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_three_one")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option


            # flow_two_three_two ---stage_three
            if payload['a_one_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_three_two ---stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_three_two")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_three_two")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            # flow_two_three_three ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_three_three ---stage_three")
            # flow_two_three_four ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_three_four ---stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_two_three_five ---stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] <  payload['a_three_closing']:
                print("flow_two_three_six ---stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_three_six")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_three_six")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option


            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_three_six ---stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_two_three_six_one ----stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_three_six_two ----stage_four")
                if payload['a_five_green'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_three_six_three ----stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_two_three_six_four ----stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_three_six_five ----stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_three_six_six ----stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_three_six_seven ----stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_two_three_six_eight ----stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_three_six_nine ----stage_four")


        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] == payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_four_one --stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_four_one")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_four_one")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option


            # flow_two_four_two --stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_four_two --stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_four_two")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_four_two")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            # flow_two_four_three --stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_four_three --stage_three")
            # flow_two_four_four --stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_four_four --stage_three")

        # flow_two_five --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_three_starts -copied")

            # flow_two_five_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_five_one --stage_three_starts")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_five_one")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_five_one")

                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            # flow_two_five_two --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_five_two --stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], weareat, True, 'two', "flow_two_five_two")
                else:
                    greenery_recording(payload['current_closing'], weareat, False, 'two', "flow_two_five_two")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option


            # flow_two_five_three --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_five_three --stage_three")
            # flow_two_five_four --stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_two_five_four --stage_three")
            # flow_two_five_five --stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_two_five_five --stage_three")

        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_three_starts_for_four --copied2")
            # flow_two_three_one ---stage_three_for_four -copied
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_two_three_one ---stage_four_starts -copied ")
                # flow_two_three_one_one ----stage_four starts
                if payload['a_five_green']:
                    print("flow_two_three_one_one ----stage_four started")

                # flow_two_three_one_two ----stage_four
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_two_three_one_two ----stage_four")


                # flow_two_three_one_three ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_three_one_three ----stage_four")

                # flow_two_three_one_four ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_three_one_four ----stage_four")


                # flow_two_three_one_five ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_three_one_five ----stage_four")


                # flow_two_three_one_six ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_one_six ----stage_four")


                # flow_two_three_one_seven ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_three_one_seven ----stage_four")



    #flow_two_one_one series going to come here -------------------------------------------"""




                # flow_two_three_one_one stage_four_starts

        # flow_two_three_two ----stage_four_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_four_starts -copied")
            # flow_two_three_two ---stage_three
            if payload['a_one_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_three_two ---stage_four_starts")

                # flow_two_three_two_one ---stage_four_starts -copied
                if payload['a_five_green']:
                    print("flow_two_three_two_one _starts_started")

                # flow_two_three_two_two
                if payload['a_five_wread'] and payload['a_five_wread'] == payload['a_four_closing']:
                    print("flow_two_three_two_two ---stage_four")

                # flow_two_three_two_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_three_two_three ---stage_four")


                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_three_two_four ---stage_four")


                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_two_five ---stage_four")


                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_three_two_six ---stage_four")

        # flow_two_three_two ----stage_four_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_four_starts -copied")
            # flow_two_three_three ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_three_three ---stage_four_starts - copied")
                # flow_two_three_three_one ------stage_four_starts
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_three_three_one ---stage_four_started")
                # flow_two_three_three_two ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_two_three_three_two ---stage_four")
                # flow_two_three_three_three ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_three_three_three ---stage_four")
                # flow_two_three_three_four ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_two_three_three_four ---stage_four")
                # flow_two_three_three_five ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_three_three_five ---stage_four")
                # flow_two_three_three_six ---stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_three_six ---stage_four")
                # flow_two_three_three_seven ---stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_three_three_seven ---stage_four")

        # flow_two_three_two ----stage_four_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_four_starts -copied")
            # flow_two_three_four ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_three_four ---stage_three")
                # flow_two_three_four_one ---stage_four_starts
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_two_three_four_one ---stage_four_started")
                # flow_two_three_four_two ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_three_four_two ---stage_three")
                # flow_two_three_four_three ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_three_four_three ---stage_three")
                # flow_two_three_four_four ---stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_four_four ---stage_three")
                # flow_two_three_four_five ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_two_three_four_five ---stage_three")





        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_four_one --stage_three -copied")
                # flow_two_four_one_one ----stage_four_starts
                if payload['a_five_green']:
                    print("flow_two_four_one_one ----stage_four_started")
                # flow_two_four_one_two ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_one_two ----stage_four")

                # flow_two_four_one_three ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_one_three ----stage_four")

                # flow_two_four_one_four ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_four_one_four ----stage_four")
                # flow_two_four_one_five ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_four_one_five ----stage_four")
                # flow_two_four_one_six ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_four_one_six ----stage_four")
                # flow_two_four_one_seven ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_four_one_seven ----stage_four")



        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_two --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_four_two --stage_three_starts_for_four - copied")
                # flow_two_four_two_one --stage_four
                if payload['a_five_green'] and payload['a_two_opens'] < payload['a_four_closing']:
                    print("flow_two_four_two_one ---stage_three_started")
                # flow_two_four_two_two --stage_three
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_two_two --stage_three")

                # flow_two_four_three --stage_three
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_three --stage_three")

                # flow_two_four_two_four --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_two_four --stage_three")

                # flow_two_four_two_five --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_two_five --stage_three")
                # flow_two_four_two_six --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_four_two_six --stage_three")

                # flow_two_four_two_seven --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_four_two_seven --stage_three")





        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_three --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_four_three --stage_three_starts_for_stage_four - copied")

                #flow_two_four_three_one ---stage_three
                if payload['a_five_green'] and payload['a_five_closing'] == payload['a_four_opens']:
                    print("flow_two_four_three_one ---stage_three_started")
                #flow_two_four_three_two ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_two_four_three_two ---stage_three")
                #flow_two_four_three_three ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_three_three ---stage_three")
                #flow_two_four_three_four ---stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_opens'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_four_three_four ---stage_three")
                #flow_two_four_three_five ---stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_four_three_five ---stage_three ---It's out of flow")



        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_four ---stage_three_starts
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_four_four --stage_three_starts_for_stage_four -copied")

                #flow_two_four_four_one ----stage_four_started
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_two_four_four_one ----stage_four_started")
                #flow_two_four_four_two ----stage_four
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_four_two ----stage_four")
                #flow_two_four_four_three ----stage_four
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_four_three ----stage_four")
                #flow_two_four_four_four ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_opens'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_four_four_four ----stage_four")
                #flow_two_four_four_five ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_four_four_five ----stage_four It's out of flow")



        # flow_two_five --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_three_starts -copied 2")

            # flow_two_five_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_five_one --stage_three_starts_for_stage_four -copied")

                #flow_two_five_one_one ----stage_four_started
                if payload['a_five_green']:
                    print("flow_two_five_one_one ----stage_four_started Verified")

                #flow_two_five_one_two --stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_five_one_two ----stage_four")

                #flow_two_five_one_three --stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_five_one_three ----stage_four")

                #flow_two_five_one_four --stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_four_opens'] < payload['a_three_closing']:
                    print("flow_two_five_one_four ----stage_four")

                #flow_two_five_one_five ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_green']:
                    print("flow_two_five_one_five ----stage_four")

                #flow_two_five_one_six ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_five_one_six ----stage_four")

                #flow_two_five_one_seven ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_five_one_seven ----stage_four")





        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_three_starts -copied 2")

            # flow_two_five_two --stage_three_starts_for_four
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_five_two --stage_three_starts_for_four copied")
                #flow_two_five_two_one  ----stage_four_started
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_two_five_two_one  ----stage_four_started")

                #flow_two_five_two_two  ----stage_four
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_five_two_two  ----stage_four")

                #flow_two_five_two_three  ----stage_four
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_five_two_three  ----stage_four")

                #flow_two_five_two_four  ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_five_two_four  ----stage_four")

                #flow_two_five_two_five  ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_five_two_five  ----stage_four")

                #flow_two_five_two_six  ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_five_two_six  ----stage_four")
                #flow_two_five_two_seven  ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_five_two_seven  ----stage_four It's our second flow")

        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_three_starts -copied 2")

            # flow_two_five_three --stage_three_starts_for_stage_four
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_five_three --stage_three_starts_for_stage_four copied")
                #flow_two_five_three_one ----stage_four_started
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_five_three_one --stage_four_started")
                #flow_two_five_three_two --stage_four
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_five_three_two --stage_four")
                #flow_two_five_three_three --stage_four
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_five_three_three --stage_four")
                #flow_two_five_three_four --stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_five_three_four --stage_four")
                #flow_two_five_three_five --stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_five_three_five --stage_four It's out of second flow")

            if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
                print("flow_two_five --stage_three_starts -copied 2")

                # flow_two_five_four --stage_three_starts_for_stage_four copied
                if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing'] and payload['a_four_opens'] > payload['a_three_closing']:
                    print("flow_two_five_four --stage_three_starts_for_stage_four copied")

                    #flow_two_five_four_one ----stage_four_started
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_two_five_four_one ----stage_four")
                    #flow_two_five_four_two ----stage_four
                    if payload['a_five_opens'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_two_five_four_two ----stage_four")
                    #flow_two_five_four_three ----stage_four
                    if payload['a_five_opens'] and payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_two_five_four_three ----stage_four")
                    #flow_two_five_four_four ----stage_four
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                        print("flow_two_five_four_four ----stage_four")
                    #flow_two_five_four_five ----stage_four
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_two_five_four_five ----stage_four It's out of second flow")
    else:
        print("It's out of second flow")










def fourth_flow(payload, time, connection_data=False, connection_obj=False):
    # if connection_data:
        # captured_output = sys.stdout = sys.stderr = open('alive/datafour.txt', 'a')
    # else:
        # captured_output = sys.stdout = sys.stderr = open('alive/datafour.txt', 'a')

    print("Now the fourth flow is at:", time)
    print("And the current closing is:", payload['current_closing'])



    if payload['a_two_wread'] and payload['a_two_opens'] < payload['a_one_closing'] and payload['a_two_wread'] and payload['a_one_green'] and payload['current_green']:
        print("a_four Entered fourth flow  - stage_one")    
        # exit()

        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_four_one -- stage_two_started")
        if payload['a_three_green'] and payload['a_three_opens'] == payload['a_two_closing']:
            print("a_four_two -- stage_two")
        if payload['a_three_wread'] and payload['a_three_opens'] < payload['a_one_closing']: 
            print("flow_four_three -- stage_two")
        if payload['a_three_wread'] and payload['a_three_opens'] == payload['a_one_closing']:
            print("a_four_four -- stage_two")
        if payload['a_three_wread'] and payload['a_one_closing'] < payload['a_three_opens'] < payload['current_closing']:
            print("flow_four_five -- stage_two")
        if payload['a_three_wread'] and payload['a_three_opens'] > payload['current_closing']:
            print("a_four_six -- stage_two")
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_four_seven -- stage_two")
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_four_eight -- stage_two")

        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_four_one -- stage_two")
            if payload['a_four_green']:
                print("flow_four_one_one -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_one_two -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_four_one_three -- stage_three")
            if payload['a_four_wread'] and payload['a_three_closing'] < payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_four_one_four -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_four_one_five -- stage_three")
            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_one_six -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_four_one_seven -- stage_three")



            if payload['a_four_green']:
                print("flow_four_one_one -- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_one_one_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_one_one_two ---- stage_four")
                if payload['a_five_wread'] and payload['a_three_closing'] < payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_four_one_one_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_one_one_four ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_one_one_five ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_one_one_six ---- stage_four")

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_one_two -- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_one_two_one ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_one_two_two ---- stage_four")
                if payload['a_five_green'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_one_two_three ---- stage_four")
                if payload['a_five_green'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_one_two_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_one_two_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_one_two_six ---- stage_four")

            if payload['a_four_wread'] and payload['a_three_closing'] < payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_four_one_four -- stage_three")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_four_one_four_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_one_four_two ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_one_four_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_one_four_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_one_four_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_one_four_six ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_one_four_seven ---- stage_four")

            # if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
            #     print("flow_four_one_six -- stage_three")
            #     if a_five_wread and a_five_opens < current_closing:
            #         print("flow_four_one_six_one ---- stage_four")
            #     if a_five_wread and a_five_opens > current_closing:
            #         print("flow_four_one_six_two ---- stage_four")
            #     if a_five_green and a_five_opens > a_four_closing:
            #         print("flow_four_one_six_three ---- stage_four")
            #     if a_five_green and a_five_opens == a_four_closing:
            #         print("flow_four_one_six_four ---- stage_four")
            #     if a_five_green and a_five_opens < a_four_closing:
            #         print("flow_four_one_six_five ---- stage_four")


                



        if payload['a_three_wread'] and payload['a_three_opens'] < payload['a_one_closing']:
            print("flow_four_three -- stage_two")

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_four_three_one -- stage_three_started")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_one_closing']:
                print("flow_four_three_two -- stage_three")
            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_three_three -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_four_three_four -- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_four_three_five -- stage_three")
            if payload['a_four_green'] and payload['a_two_closing'] < payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_three_six -- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_two_closing']:
                print("flow_four_three_seven -- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_four_three_eight -- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_four_three_nine -- stage_three")


            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_four_three_one -- stage_three_started")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_four_three_one_one -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_three_one_two -- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_three_one_three -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_three_one_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_one_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_three_one_six ---- stage_four")
                if payload['a_five_green'] and payload['a_three_closing'] < payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_one_seven ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_three_one_eight ---- stage_four")
                if payload['a_five_green'] and payload['a_three_closing'] > payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_four_three_one_nine ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_three_one_ten ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_three_one_eleven ---- stage_four")

            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_three_three -- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_four_three_three_one -- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_three_three_two -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_three_three -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_three_three_four -- stage_four")
                if payload['a_five_wread'] and payload['a_three_closing'] < payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_three_five -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_three_three_six -- stage_four")
                if payload['a_five_wread'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_three_three_seven -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_three_three_eight -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_three_three_nine -- stage_four")

            if payload['a_four_green'] and payload['a_two_closing'] < payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_three_six -- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_four_three_six_one ---- stage_four")


                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_three_six_two ---- stage_four")

                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_four_three_six_three ---- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_three_six_four ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_three_six_five ---- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_six_six ---- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] == payload['a_five_opens']:
                    print("flow_four_three_six_seven ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_three_six_eight ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_three_six_nine ---- stage_four")

            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_four_three_eight -- stage_three")

                if payload['a_five_green']:
                    print("flow_four_three_eight_one ---- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_three_eight_two -- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_three_eight_three -- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] < payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_eight_four -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_three_eight_five -- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_three_eight_six -- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_three_eight_seven -- stage_four")



            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_four_three_nine -- stage_three")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_three_nine_one ---- stage_four")

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_three_nine_two ---- stage_four")

                if payload['a_five_green'] and payload['a_four_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_three_nine_three ---- stage_four")

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_three_nine_four ---- stage_four")

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_three_nine_five ---- stage_four")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_three_nine_six ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_three_nine_seven ---- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_three_nine_eight ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_three_nine_nine ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_three_nine_ten ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_three_nine_eleven ---- stage_four")


        if payload['a_three_wread'] and payload['a_one_closing'] < payload['a_three_opens'] < payload['current_closing']:
            print("flow_four_five -- stage_two")

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_five_one --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_four_five_two --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_four_five_three --- stage_three")
            if payload['a_four_green'] and payload['a_two_closing'] < payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_five_four --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_four_five_five --- stage_three")

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_five_one --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_four_five_one_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_five_one_two ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_five_one_three ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_five_one_four ---- stage_four")
                if payload['a_five_green'] and payload['a_four_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_five_one_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_five_one_six ---- stage_four")
                if payload['a_five_green'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_five_one_seven ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_five_one_eight ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_five_one_nine ---- stage_four")

            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_four_five_three --- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_five_three_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_three_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_three_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_five_three_two ---- stage_four")
                if payload['a_five_green'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_five_three_three ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_five_three_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_five_three_five ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_three_five")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_three_five")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_five_three_six ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_three_six")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_three_six")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_five_three_seven ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_three_seven")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_three_seven")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_five_three_eight ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_three_eight")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_three_eight")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_five_three_nine ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_three_nine")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_three_nine")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


            if payload['a_four_green'] and payload['a_two_closing'] < payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_five_four --- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_four_five_four_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_four_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_four_one")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_five_four_two ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_four_two")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_four_two")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_five_four_three ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_four_three")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_four_three")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_five_four_four ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_four_four")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_four_four")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_five_four_five ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_five_four_six ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_five_four_seven ---- stage_four")


            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_four_five_five --- stage_three")

                if payload['a_five_green']:
                    print("flow_four_five_five_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_five_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_five_one")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_five_five_two --- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'four', "flow_four_five_five_two")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'four', "flow_four_five_five_two")

                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_five_five_three --- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_five_five_four --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_five_five_five --- stage_four")
                # print("spfdsfkpsd:", payload)
                # exit()


        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_four_seven -- stage_two")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_four_seven_one --- stage_three_started")
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_two_closing']:
                print("flow_four_seven_two --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_four_seven_three --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_seven_four --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_four_seven_five --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_four_seven_six --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_one_closing']:
                print("flow_four_seven_seven --- stage_three")
            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_seven_eight --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_four_seven_seven --- stage_three")


            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_seven_eight --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_four_seven_eight_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_seven_eight_two ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_seven_eight_three ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_seven_eight_four ---- stage_four")
                if payload['a_five_green'] and payload['a_four_closing'] > payload['a_five_opens'] > payload['a_three_opens']:
                    print("flow_four_seven_eight_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_opens']:
                    print("flow_four_seven_eight_six ---- stage_four")
                if payload['a_five_green'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_opens']:
                    print("flow_four_seven_eight_seven ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_seven_eight_eight ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_seven_eight_nine ---- stage_four")



            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['current_closing']:
                print("flow_four_seven_six --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_four_seven_six_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens']  == payload['a_one_closing']:
                    print("flow_four_seven_six_two ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_seven_six_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_seven_six_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_seven_six_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_seven_six_six ---- stage_four")
                if payload['a_five_green'] and payload['a_three_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_seven_six_seven ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_seven_six_eight ---- stage_four")
                if payload['a_five_green'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_seven_six_nine ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_seven_six_ten ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_seven_six_eleven ---- stage_four")






                if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                    print("flow_four_seven_four --- stage_three")

                    if payload['a_five_green'] and payload['a_five_opens'] < payload['a_three_closing']:
                        print("flow_four_seven_four_one --- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                        print("flow_four_seven_four_two --- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                        print("flow_four_seven_four_three ---- stage_four")
                    if payload['a_five_green'] and payload['a_five_opens'] == payload['a_one_closing']:
                        print("flow_four_seven_four_four ---- stage_four")
                    if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                        print("flow_four_seven_four_five ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                        print("flow_four_seven_four_six ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                        print("flow_four_seven_four_seven ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing']:
                        print("flow_four_seven_four_eight ---- stage_four")
                    if payload['a_five_wread'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                        print("flow_four_seven_four_nine ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_two_closing']:
                        print("flow_four_seven_four_ten ---- stage_four")
                    if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                        print("flow_four_seven_four_eleven ---- stage_four")



            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_four_seven_one --- stage_three_started")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_four_seven_one_one --- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_four_seven_one_two --- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_four_seven_one_three --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_seven_one_four --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_seven_one_five --- stage_four")
                if payload['a_five_wread'] and payload['a_three_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_seven_one_six --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_seven_one_seven --- stage_four")
                if payload['a_five_wread'] and payload['a_three_closing'] < payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_four_seven_one_eight --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_seven_one_nine --- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_seven_one_ten --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_seven_one_eleven --- stage_four")



            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_four_seven_three --- stage_three")

                if payload['a_five_green']:
                    print("flow_four_seven_three_one --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_seven_three_two --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_seven_three_three --- stage_four")
                if payload['a_five_wread'] and payload['a_three_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_seven_three_four --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_seven_three_five ---- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_seven_three_six ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_seven_three_seven --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_seven_three_eight --- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_seven_three_nine --- stage_four")




        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_four_eight -- stage_two")
            if payload['a_four_green']:
                print("flow_four_eight_one --- stage_three_started")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_eight_two --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_four_eight_three --- stage_three")
            if payload['a_four_wread'] and payload['a_one_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_four_eight_four --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_one_closing']:
                print("flow_four_eight_five --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_one_closing']:
                print("flow_four_eight_six --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_four_eight_seven --- stage_three")


            if payload['a_four_green']:
                print("flow_four_eight_one --- stage_three_started")

                if payload['a_five_green']:
                    print("flow_four_eight_one_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_eight_one_two ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_eight_one_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_three_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_eight_one_four ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_eight_one_five ---- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_eight_one_six ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_eight_one_seven ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_eight_one_eight ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_eight_one_nine ---- stage_four")

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_four_eight_two --- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_eight_two_one ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_eight_two_two ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_four_eight_two_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_four_eight_two_four ---- stage_four")
                if payload['a_five_wread'] and payload['a_one_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_four_eight_two_five ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_four_eight_two_six ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_eight_two_seven ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_eight_two_eight ---- stage_four")

            if payload['a_four_wread'] and payload['a_one_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_four_eight_four --- stage_three")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_eight_four_one ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_eight_four_two ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_eight_four_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_four_eight_four_four ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_four_eight_four_five ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_eight_four_six ---- stage_four")


            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_one_closing']:
                print("flow_four_eight_six --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_four_eight_six_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_four_eight_six_two ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_four_eight_six_three ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_four_eight_six_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_four_eight_six_five ---- stage_four")









def high_fiveflow(payload, time, connection_data=False, connection_obj=False):
    # if connection_data:
        # captured_output = sys.stdout = sys.stderr = open('alive/highfivedata.txt', 'a')
    # else:
        # captured_output = sys.stdout = sys.stderr = open('highfivedata.txt', 'a')
    print("High fiving at:", time)
    if payload['current_green'] and payload['a_one_wread'] and payload['a_two_wread'] and payload['a_one_opens'] < payload['a_two_opens'] < payload['current_closing']:
        print("flow_five Welcome to high five flow")

        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_five_one -- stage_two_started")
        if payload['a_three_green'] and payload['a_three_opens'] == payload['a_two_closing']:
            print("flow_five_two -- stage_two")
        if payload['a_three_green'] and payload['a_one_closing'] < payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_five_three -- stage_two")
        if payload['a_three_green'] and payload['a_three_opens'] == payload['a_one_closing']:
            print("flow_five_four -- stage_two")
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_one_closing']:
            print("flow_five_five -- stage_two")
        if payload['a_three_wread'] and payload['a_three_opens'] < payload['current_closing']:
            print("flow_five_six -- stage_two")
        if payload['a_three_wread'] and payload['a_three_opens'] > payload['current_closing']:
            print("flow_five_seven -- stage_two")



        if payload['a_three_green'] and payload['a_one_closing'] < payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_five_three -- stage_two")

            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_one_closing']:
                print("flow_five_three_one -- stage_three_started")

                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_three_one")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_three_one")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_one_closing']:
                print("flow_five_three_two -- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_three_two")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_three_two")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_five_three_three -- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_three_three")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_three_three")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option


            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_five_three_four -- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_three_four")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_three_four")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_five_three_five -- stage_three")
            if payload['a_four_wread'] and payload['current_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_five_three_six -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_five_three_seven -- stage_three")

        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_one_closing']:
            print("flow_five_five -- stage_two")

            if payload['a_four_green']:
                print("flow_five_five_one --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_five_one")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_five_one")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option



            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_five_five_two -- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_five_two")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_five_two")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_five_five_three -- stage_three")
            if payload['a_four_wread'] and payload['current_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_five_five_four -- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_five_five_five -- stage_three")

        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_five_one -- stage_two_started")

            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_five_one_one --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_one_one")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_one_one")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_two_closing']:
                print("flow_five_one_two --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_one_two")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_one_two")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_green'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_five_one_three --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_one_three")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_one_three")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_one_closing']:
                print("flow_five_one_four --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_one_four")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_one_four")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_five_one_five --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_one_five")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_one_five")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_five_one_six --- stage_three")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if (payload['highest_price_one'] < payload['a_two_opens']):
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                    greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_one_six")
                else:
                    greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_one_six")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                    print("Resultant option:", resultant_option)
                    return resultant_option

            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_five_one_seven --- stage_three")
            if payload['a_four_wread'] and payload['current_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_five_one_eight --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_five_one_nine --- stage_three")



        if payload['a_three_wread'] and payload['a_three_opens'] < payload['current_closing']:
            print("flow_five_six -- stage_two")

            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_five_six_one --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_five_six_two --- stage_three")
            if payload['a_four_green'] and payload['a_three_closing'] > payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_five_six_three --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_two_closing']:
                print("flow_five_six_four --- stage_three")
            if payload['a_four_green'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_five_six_five --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_one_closing']:
                print("flow_five_six_six --- stage_three")
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_five_six_seven --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_five_six_eight --- stage_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_five_six_nine --- stage_three")


            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_five_six_one --- stage_three")

                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_five_six_one_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_five_six_one_two ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_two")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_two")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_five_six_one_three ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_three")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_three")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_five_six_one_four ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_four")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_four")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_one_closing'] < payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_five_six_one_five ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_five")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_five")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_five_six_one_six ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_six")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_six")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_five_six_one_seven ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_seven")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_seven")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_five_six_one_eight ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_five_six_one_nine ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_five_six_one_ten ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_one_ten")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_one_ten")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option



            if payload['a_four_green'] and payload['a_three_closing'] > payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_five_six_three --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_five_six_three_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_three_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_three_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_five_six_three_two ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_five_six_three_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_four_closing'] < payload['a_five_opens'] < payload['current_closing']:
                    print("flow_five_six_three_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("flow_five_six_three_five ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_three_five")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_three_five")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_five_six_three_six ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_three_six")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_three_six")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_one_closing'] < payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_five_six_three_seven ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_three_seven")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_three_seven")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_five_six_three_eight ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_three_eight")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_three_eight")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_five_six_three_nine ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_three_nine")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_three_nine")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option


            if payload['a_four_green'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_five_six_five --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_five_six_five_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_five_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_five_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_five_six_five_two ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_five_six_five_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_five_six_five_four ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_one_closing']:
                    print("flow_five_six_five_five ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_five_five")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_five_five")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_five_six_five_six ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_five_six")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_five_six")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_five_six_five_seven ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_five_seven")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_five_seven")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option



            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_one_closing']:
                print("flow_five_six_seven --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_five_six_seven_one ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_seven_one")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_seven_one")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_five_six_seven_two ---- stage_four")
                if payload['a_five_wread'] and payload['current_closing'] > payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_five_six_seven_three ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_five_six_seven_four ---- stage_four")
                if payload['a_five_green']:
                    print("flow_five_six_seven_five ---- stage_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if (payload['highest_price_one'] < payload['a_three_opens']) or (payload['highest_price_two'] < payload['a_three_opens']):
                        print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Confirmed")
                        greenery_recording(payload['current_closing'], time, True, 'five', "flow_five_six_seven_five")
                    else:
                        greenery_recording(payload['current_closing'], time, False, 'five', "flow_five_six_seven_five")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "CE")
                        print("Resultant option:", resultant_option)
                        return resultant_option

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_five_six_eight --- stage_three")

                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_five_six_eight_one ---- stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_five_six_eight_two --- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_five_six_eight_three ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_five_six_eight_four ---- stage_four")
                if payload['a_five_green'] and payload['a_three_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_five_six_eight_five ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_five_six_eight_six ---- stage_four")
                if payload['a_five_green'] and payload['a_two_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_five_six_eight_seven ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_five_six_eight_eight ---- stage_four")
                if payload['a_five_green'] and payload['a_one_closing'] < payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_five_six_eight_nine ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_one_closing']:
                    print("flow_five_six_eight_ten ---- stage_four")
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_one_closing']:
                    print("flow_five_six_eight_eleven ---- stage_four")
