import MetaTrader5 as mt5

if not mt5.initialize():
    print("MT5 Connection Failed")
    quit()

symbols = mt5.symbols_get()

for symbol in symbols:
    print(symbol.name)

mt5.shutdown()