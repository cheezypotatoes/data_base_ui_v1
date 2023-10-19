import sqlite3

def create_table():
    # Connect to the SQLite database
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Define the table schema
    table_name = "person_info"

    # Check if the table exists and create it if it doesn't
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute(f'''
            CREATE TABLE {table_name} (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                gender TEXT,
                age INTEGER,
                birth_date DATE,
                precinct_number TEXT,
                sector TEXT,
                organization TEXT,
                civil_status TEXT,
                house_number TEXT
            )
        ''')
        conn.commit()
    conn.close()


def check_data():
    create_table()  # Call create_table to ensure the table exists

    # Connect to the SQLite database
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Retrieve and display all records
    cursor.execute("SELECT first_name,"
                   " last_name, gender,"
                   " age, birth_date,"
                   " precinct_number,"
                   " sector,"
                   " organization,"
                   " civil_status,"
                   " house_number"
                   " FROM person_info")
    records = cursor.fetchall()

    conn.close()

    if not records:
        return [["NO DATA"]]

    result = []

    for record in records:
        result.append(list(record))

    return result






