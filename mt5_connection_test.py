import MetaTrader5 as mt5

connected = mt5.initialize()

if connected:
    print("CONNECTED TO MT5")
    print(mt5.terminal_info())
    print(mt5.account_info())
else:
    print("FAILED TO CONNECT")
    print(mt5.last_error())

mt5.shutdown()