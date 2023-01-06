import mt5

# Connect to the MetaTrader 5 terminal
mt5.initialize()

# Fetch the data for the EURUSD, GBPUSD, and CHFUSD currency pairs
eurusd_data = mt5.copy_rates_from('EURUSD', mt5.TIMEFRAME_M1, datetime.datetime.now() - datetime.timedelta(days=1), 1000)
gbpusd_data = mt5.copy_rates_from('GBPUSD', mt5.TIMEFRAME_M1, datetime.datetime.now() - datetime.timedelta(days=1), 1000)
chfusd_data = mt5.copy_rates_from('CHFUSD', mt5.TIMEFRAME_M1, datetime.datetime.now() - datetime.timedelta(days=1), 1000)

# Convert the data to pandas dataframes
eurusd_df = pd.DataFrame(eurusd_data)
gbpusd_df = pd.DataFrame(gbpusd_data)
chfusd_df = pd.DataFrame(chfusd_data)

# Calculate the correlation between the EURUSD and GBPUSD pairs
correlation = eurusd_df['close'].corr(gbpusd_df['close'])

# If the correlation is positive, then buy EURUSD and sell GBPUSD
if correlation > 0:
    # Place a buy order for EURUSD
    result = mt5.order_send('EURUSD', mt5.ORDER_TYPE_BUY, 100000, 1.2050)
    if result == 0:
        print("EURUSD buy order placed successfully")
    else:
        print("Error placing EURUSD buy order")

    # Place a sell order for GBPUSD
    result = mt5.order_send('GBPUSD', mt5.ORDER_TYPE_SELL, 100000, 1.3550)
    if result == 0:
        print("GBPUSD sell order placed successfully")
    else:
        print("Error placing GBPUSD sell order")

# If the correlation is negative, then sell EURUSD and buy GBPUSD
elif correlation < 0:
    # Place a sell order for EURUSD
    result = mt5.order_send('EURUSD', mt5.ORDER_TYPE_SELL, 100000, 1.2050)
    if result == 0:
        print("EURUSD sell order placed successfully")
    else:
        print("Error placing EURUSD sell order")

    # Place a buy order for GBPUSD
    result = mt5.order_send('GBPUSD', mt5.ORDER_TYPE_BUY, 100000, 1.3550)
    if result == 0:
