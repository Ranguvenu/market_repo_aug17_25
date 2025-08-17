import pandas as pd
import sys
from db import *
from optionslib import *

# def flowfilter(payload, timeofcalling, connection_data=False, connection_obj=False):

def bear_one(payload, timeofcalling, connection_data=False, connection_obj=False):
    print("This is current closing:",payload['current_closing'])
    print("Testing at:", timeofcalling)

    # print("bear_three_three_two_two")
    # print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # if connection_data:
    #     resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
    #     greenery_recording(payload['current_closing'], timeofcalling, True, 'one')
    #     print("Resultant option:", resultant_option)
    #     return resultant_option
    # print("bear_one_one_one_one")
    # print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # if connection_data:
    #     resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
    #     greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_one_one")
    #     print("Resultant option:", resultant_option)
    #     return resultant_option

    if payload['current_wread'] and payload['a_one_wread'] and payload['a_two_green'] and payload['a_two_opens'] > payload['a_one_closing']:
        print("bear_one")

        if payload['a_three_green'] and payload['current_closing'] < payload['a_three_opens'] < payload['a_one_closing']:
            print("bear_one_one")

            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_one_one_one")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_one_one_one_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_one_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_one_one_one_two")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("bear_one_one_one_three")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_one_three")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_wread'] and payload['a_two_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("bear_one_one_one_four")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_one_four")
                        print("Resultant option:", resultant_option)
                        return resultant_option

            if payload['a_four_wread'] and payload['a_two_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_one_one_two")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_one_one_two_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_two_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_one_one_two_two")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("bear_one_one_two_three")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_two_three")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_one_one_two_four>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_two_four")
                        print("Resultant option:", resultant_option)
                        return resultant_option

            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("bear_one_one_three")
                if payload['a_five_wread']:
                    print("bear_one_one_three_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_three_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_one_one_three_two")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_one_one_three_two")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_one_one_three_three")

            if payload['a_four_green'] and payload['a_four_opens'] > payload['current_closing']:
                print("bear_one_one_four")

        if payload['a_three_opens'] > payload['a_one_closing'] and payload['a_three_green']:
            print("bear_one_two")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['current_closing']:
                print("bear_one_two_one")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_one_closing']:
                print("bear_one_two_two")
            if payload['a_four_green'] and payload['a_one_closing'] < payload['a_four_opens'] > payload['current_closing']:
                print("bear_one_two_three")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_one_two_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_one_two_four_one")
                if payload['a_five_wread'] and payload['a_three_closing'] < payload['a_five_opens'] < payload['a_two_closing']:
                    print("bear_one_two_four_two")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("bear_one_two_four_three")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_one_two_four_four")
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_two_closing']:
                    print("bear_one_two_four_five")
                if payload['a_five_green'] and payload['a_four_closing'] > payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_one_two_four_six")

            if payload['a_four_wread'] and payload['a_two_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_one_two_five")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_one_two_five_one")
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_one_two_five_two")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_one_two_five_three")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("bear_one_two_five_four")

            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("bear_one_two_six_one")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_one_two_six_two")
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_one_two_six_three")
                if payload['a_five_wread']:
                    print("bear_one_two_six_four")

        if payload['a_three_wread'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("bear_one_three")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("bear_one_three_one")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("bear_one_three_two")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_one_three_three")
            if payload['a_four_wread'] and payload['a_one_closing'] < payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_one_three_four")
            if payload['a_four_wread'] and payload['current_closing'] < payload['a_four_opens'] < payload['a_one_closing']:
                print("bear_one_three_five")

        if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("bear_one_four")
            if payload['a_four_wread']:
                print("bear_one_four_one")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_one_four_two")
            if payload['a_four_green'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_one_four_three")
            if payload['a_four_green'] and payload['current_closing'] < payload['a_four_opens'] < payload['a_one_closing']:
                print("bear_one_four_four")





def bear_two(payload, timeofcalling, connection_data=False, connection_obj=False):
    if payload['a_two_green'] and payload['a_one_wread'] and payload['current_wread'] and payload['current_closing'] < payload['a_two_opens'] < payload['a_one_closing']:
        print("bear_two")
        if payload['a_three_wread'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("bear_two_one")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_two_one_one")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                    greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_one_one")
                    print("Resultant option:", resultant_option)
                    return resultant_option
            if payload['a_four_green'] and payload['current_closing'] < payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_two_one_two")
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                    greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_one_three")
                    print("Resultant option:", resultant_option)
                    return resultant_option
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("bear_two_one_four")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                    greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_one_four")
                    print("Resultant option:", resultant_option)
                    return resultant_option

        if payload['a_three_green'] and payload['a_three_opens'] > payload['current_closing']:
            print("bear_two_two")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_two_two_one")
                if payload['a_five_wread'] and payload['a_two_closing'] > payload['a_five_opens'] > payload['a_three_closing']:
                    print("bear_two_two_one_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_one_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_two_two_one_two")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_one_two")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['a_four_closing'] > payload['a_five_opens'] > payload['current_closing']:
                    print("bear_two_two_one_three")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_two_two_one_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("bear_two_two_one_five")

            if payload['a_four_wread'] and payload['a_two_closing'] > payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_two_two_two")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_two_closing']:
                    print("bear_two_two_two_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_two_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("bear_two_two_two_two")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_two_two")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_two_two_two_three")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_two_three")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_two_two_two_four")

            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("bear_two_two_three")
                if payload['a_five_wread']:
                    print("bear_two_two_three_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_three_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_two_two_three_two")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_two_three_two")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_two_two_three_three")

        if payload['a_three_wread'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("bear_two_three")
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_two_three_one")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                    greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_three_one")
                    print("Resultant option:", resultant_option)
                    return resultant_option
            if payload['a_four_wread']:
                print("bear_two_three_two")
                print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if connection_data:
                    resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                    greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_two_three_two")
                    print("Resultant option:", resultant_option)
                    return resultant_option
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_two_three_three")



def bear_three(payload, timeofcalling, connection_data=False, connection_obj=False):
    if payload['a_one_wread'] and payload['a_two_wread'] and payload['current_wread']:
        print("bear_three")
        if payload['a_three_green'] and payload['a_four_opens'] > payload['a_two_closing']:
            print("bear_three_one")
            if payload['a_four_green'] and payload['a_one_closing'] > payload['a_four_opens']:
                print("bear_three_one_four")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_three_one_four_one")

        if payload['a_three_green'] and payload['a_one_closing'] < payload['a_four_opens'] < payload['a_two_closing']:
            print("bear_three_two")

        if payload['a_three_green'] and payload['a_one_closing'] > payload['a_three_opens'] > payload['current_closing']:
            print("bear_three_three")
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("bear_three_three_one")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("bear_three_three_one_one")
                    print("bear_one_one_three_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_three_one_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("bear_three_three_one_two")
                    print("bear_one_one_three_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_three_one_two")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_three_three_one_three")
                    print("bear_one_one_three_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_three_one_three")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_three_three_one_four")

            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("bear_three_three_two")
                if payload['a_five_wread']:
                    print("bear_three_three_two_one")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_three_two_one")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("bear_three_three_two_two")
                    print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    if connection_data:
                        resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
                        greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_three_two_two")
                        print("Resultant option:", resultant_option)
                        return resultant_option
                if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_three_three_two_three")

            if payload['a_four_green'] and payload['a_four_opens'] > payload['current_closing']:
                print("bear_three_three_three")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("bear_three_three_three_one")
                if payload['a_five_wread'] and payload['a_four_closing'] < payload['a_five_opens'] < payload['a_three_closing']:
                    print("bear_three_three_three_two")
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("bear_three_three_three_three")
                if payload['a_five_green'] and payload['a_five_opens'] > payload['current_closing']:
                    print("bear_three_three_three_four")

        # if payload['a_three_green']:
        #     print("bear_three_four")
        #     if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
        #         print("bear_three_four_one")
        #         if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_three_closing']:
        #             print("bear_three_four_one_one")
        #             print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #             if connection_data:
        #                 resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
        #                 greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_four_one_one")
        #                 print("Resultant option:", resultant_option)
        #                 return resultant_option
        #         if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
        #             print("bear_three_four_one_two")
        #             print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #             if connection_data:
        #                 resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
        #                 greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_four_one_two")
        #                 print("Resultant option:", resultant_option)
        #                 return resultant_option
        #         if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
        #             print("bear_three_four_one_three")
        #         if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing']:
        #             print("bear_three_four_one_four")
        #             print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #             if connection_data:
        #                 resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
        #                 greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_four_one_four")
        #                 print("Resultant option:", resultant_option)
        #                 return resultant_option
        #     if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing']:
        #         print("bear_three_four_two")
        #         if payload['a_five_wread']:
        #             print("bear_three_four_two_one")
        #             print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #             if connection_data:
        #                 resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
        #                 greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_four_two_one")
        #                 print("Resultant option:", resultant_option)
        #                 return resultant_option
        #         if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
        #             print("bear_three_four_two_two")
        #             print("Greening from here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #             if connection_data:
        #                 resultant_option = pickup_fromstream(connection_obj, connection_data, "PE")
        #                 greenery_recording(payload['current_closing'], timeofcalling, True, 'one', "bear_three_four_two_two")
        #                 print("Resultant option:", resultant_option)
        #                 return resultant_option
        #         if payload['a_five_green'] and payload['current_closing'] < payload['a_five_opens'] < payload['a_four_closing']:
        #             print("bear_three_four_two_three")

        #     if payload['a_four_green'] and payload['a_four_opens'] > payload['current_closing']:
        #         print("bear_three_four_three")
