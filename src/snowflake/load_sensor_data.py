
import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

conn = None
cursor = None

try:
    # Connect to Snowflake
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

    # Read sensor CSV
    df = pd.read_csv("data/sensor_readings.csv")

    print("CSV loaded successfully!")
    print("Total records:", len(df))

    # Prepare insert query
    insert_query = """
        INSERT INTO SENSOR_READINGS
        (SHIPMENT_ID, TIMESTAMP, TEMPERATURE_C,
         HUMIDITY_PERCENT, VIBRATION_G)
        VALUES (%s, %s, %s, %s, %s)
    """

    # Convert rows and insert
    rows = [
        (
            row.shipment_id,
            pd.to_datetime(row.timestamp).to_pydatetime(),
            float(row.temperature_c),
            float(row.humidity_percent),
            float(row.vibration_g)
        )
        for row in df.itertuples(index=False)
    ]

    cursor.executemany(insert_query, rows)
    conn.commit()

    print("Data inserted into Snowflake successfully!")
    print("Records inserted:", len(rows))

except Exception as e:
    if conn:
        conn.rollback()
    print("Data loading failed!")
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
