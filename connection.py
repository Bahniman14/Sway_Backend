# from database import create_connection
import psycopg2

# DB_FILE = "sway_database.db"  # Update this with your actual database file path

# # Create connection to SQLite database
# conn = create_connection(DB_FILE)

# if conn is None:
#     print("Error: Unable to connect to the database.")
#     exit()

DB_HOST = "dpg-coj5qs8l5elc73didj50-a.oregon-postgres.render.com"
DB_NAME = "swaydatabase"
DB_USER = "swaydatabase_user"
DB_PASSWORD = "nO4TKDvO5m4dUAahbCzelt8yRul4b2gF"

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    print("Successfully connected to the database.")
except psycopg2.Error as e:
    print(f"Error: Unable to connect to the database: {e}")
    exit()