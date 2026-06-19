import MetaTrader5 as mt5

mt5.initialize()

symbols = mt5.symbols_get()

print(f"Total Symbols: {len(symbols)}")
print("-" * 50)

for symbol in symbols:
    print(symbol.name)

mt5.shutdown()