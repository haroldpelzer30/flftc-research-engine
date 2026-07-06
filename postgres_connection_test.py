from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

host = os.getenv("POSTGRES_HOST")
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")

print("Testing connection...")

conn = psycopg2.connect(
    host=host,
    dbname=database,
    user=user,
    password=password,
    port=port,
    sslmode="require"
)

print("Connected successfully!")

conn.close()
print("Connection closed.")