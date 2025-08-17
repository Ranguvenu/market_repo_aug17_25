def stream_into_flow(connection_obj, connection_data):
    i = 0
    while True:
        # captured_outputs = sys.stdout = sys.stderr = open('data.txt', 'a')

        # time.sleep(2)  # Sleep for "Intervel" seconds before running again
        live_history_params = recent_number_of_histories_params_forlive("NSE", "99926009", "FIVE_MINUTE", 12, 5, False, False)

        current_params = recent_number_of_histories_params_forlive("NSE", "99926009", "FIVE_MINUTE", 0, 5, False, True)

        # current_history = obj.getCandleData(current_params)
        try:
            history = connection_obj.getCandleData(live_history_params)
            current_history = connection_obj.getCandleData(current_params)
        except Exception as e:
            print("Not got candles. And the error is:", e)
            #login api call
            history = connection_obj.getCandleData(live_history_params)
            current_history = connection_obj.getCandleData(current_params)


        Historion = recent_history_forflowing(history)

        current = current_flowing(current_history)
        if not current:
            print("this is current params:", current_params)
            print("this is current:", current)

        Historion.update(current)

        flowfilter(Historion, current_params['todate'], connection_data, connection_obj)

        flow_two(Historion, current_params['fromdate'], connection_data, connection_obj)


        fourth_flow(Historion, current_params['todate'], connection_data, connection_obj)
        high_fiveflow(Historion, current_params['todate'], connection_data, connection_obj)


        # save_tofile = flow_two(Historion)
        # next_fivemloop_insecondss = next_fivemloop_inseconds()
        # save_data(save_tofile)
        i += 1
        print("after flow"+str(i))

        # time.sleep(next_fivemloop_inseconds())  # Sleep for "Intervel" seconds before running again
        if next_fivemloop_inseconds() != 0:
            time.sleep(next_fivemloop_inseconds())  # Sleep for "Intervel" seconds before running again
        elif next_fivemloop_inseconds() <= 0:
            time.sleep(300)
