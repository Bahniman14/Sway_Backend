from database import create_connection

DB_FILE = "sway_database.db"  # Update this with your actual database file path

# Create connection to SQLite database
conn = create_connection(DB_FILE)

if conn is None:
    print("Error: Unable to connect to the database.")
    exit()