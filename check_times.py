import duckdb

conn = duckdb.connect("flftc_research.duckdb")

df = conn.execute("""
SELECT DISTINCT trade_time
FROM eurusd_h4
ORDER BY trade_time
""").fetchdf()

print(df)