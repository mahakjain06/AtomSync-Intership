
import os
import snowflake.connector
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv(override=True)

try:
    conn = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE")
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            CURRENT_ACCOUNT(),
            CURRENT_USER(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA(),
            CURRENT_WAREHOUSE()
    """)

    result = cursor.fetchone()

    print("\nSnowflake Connection Successful!")
    print("Account:", result[0])
    print("User:", result[1])
    print("Database:", result[2])
    print("Schema:", result[3])
    print("Warehouse:", result[4])

    cursor.close()
    conn.close()

except Exception as e:
    print("Snowflake Connection Failed!")
    print("Error:", e)
