import duckdb

conn = duckdb.connect("flftc_research.duckdb")

conn.execute("""
CREATE OR REPLACE TABLE usdchf_h4 AS
SELECT
    column0 AS trade_date,
    column1 AS trade_time,
    column2 AS open,
    column3 AS high,
    column4 AS low,
    column5 AS close,
    column6 AS volume
FROM usdchf_h4
""")

print(conn.execute("DESCRIBE usdchf_h4").fetchall())