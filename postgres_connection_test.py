import os
import psycopg2
from dotenv import load_dotenv

# Load .env file from the current folder
load_dotenv()

# Show whether variables are loading
print("Checking environment variables...")
print("POSTGRES_HOST =", os.getenv("POSTGRES_HOST"))
print("POSTGRES_DB =", os.getenv("POSTGRES_DB"))
print("POSTGRES_USER =", os.getenv("POSTGRES_USER"))
print("POSTGRES_PORT =", os.getenv("POSTGRES_PORT"))
print("POSTGRES_PASSWORD loaded =", "YES" if os.getenv("POSTGRES_PASSWORD") else "NO")
print("-" * 60)

try:
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        sslmode="require"
    )

    print("SUCCESSFULLY CONNECTED TO AZURE POSTGRES")

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()

    print("\nPostgres Version:")
    print(version[0])

    cursor.close()
    conn.close()

    print("\nConnection closed.")

except Exception as e:
    print("CONNECTION FAILED")
    print(e)