def forword_testing(connection_object, current_time, history_time, connection_data):
    # captured_output = sys.stdout = sys.stderr = open('forword_records/libprints.txt', 'a')

    index_targets = []

    i = 0
    while True:
        time.sleep(1)  # Sleep for "Intervel" seconds before running again

        history_time = next_times_giving(history_time)
        current_time = next_times_giving(current_time)

        try:
            params = recent_number_of_forwording_histories_params("NSE", "99926009", "FIVE_MINUTE", 6, 5, history_time)
            current_params = recent_number_of_forwording_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_time)

            history = connection_object.getCandleData(params)
            current_history = connection_object.getCandleData(current_params)

            try:
                current_history = connection_object.getCandleData(current_params)
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

            try:
                current = current_flowing(current_history)
            except Exception as e:
                print('the error is:')
                print(f"Error while selling: {e}")
                exit()


            if not current:
                print("this is current params:", current_params)
                print("this is current:", current)

            Historion.update(current)

            flowfilterv = flowfilter(Historion, current_params['todate'], connection_data, connection_object)
            flow_twov = flow_two(Historion, current_params['todate'], connection_data, connection_object)

            fourth_flowv = fourth_flow(Historion, current_params['todate'], connection_data, connection_object)
            high_fiveflowv = high_fiveflow(Historion, current_params['todate'], connection_data, connection_object)

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            variables = [flowfilterv, flow_twov, fourth_flowv, high_fiveflowv]
            print("variables:::::", variables)
            for var in variables:
                print("var of variable:", var)
                if var is not None:
                    # print("IF Not none:", var)
                    # exit()
                    bounds = [51966.51, 52186.93, 52460.21, 52701.59, 52998.74, 53182.99]

                    lower_bound, upper_bound = find_bounds(bounds, Historion['current_closing'], margin = 51)
                    # print(upper_bound)
                    # print(Historion['current_closing'])
                    # exit()
                    option_order_response = option_order_record(connection_object, var, "BUY", Historion['current_closing'], upper_bound)
                    print("option_order_response::", option_order_response)
                    # exit()
                    # if var > 0:
                    #     if var not in index_targets:
                    #         index_targets.append(var)
                    # elif var < 0:
                    #     if -var in index_targets:
                    #         index_targets.remove(-var)
            entered_options = get_entered_options()
            print("entered_options: ", entered_options)
            # exit()
            if entered_options:
                fast_looping(connection_object, entered_options, Historion['current_closing'])

            holdings = True
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # holdings = False
            # if flowfilterv or flow_twov or fourth_flowv or high_fiveflowv or holdings:
            # sleep_time = next_fivemloop_inseconds()
            print('in usual 5 seconds loop')

            time.sleep(5)
            i += 1
            print("after flow"+str(i))


            # Place your main function logic here that runs after the sleep period.
        except Exception as e:
            return {'history_date': history_time, 'current_date': current_time}
    return {'history_date':history_date, 'current_date':current_date}

