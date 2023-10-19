import sqlite3

def check_data(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Define the table schema
    table_name = "person_info"

    # Check if the table exists
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    table_exists = cursor.fetchone()

    if not table_exists:
        conn.close()
        return "Table 'person_info' does not exist in the database."

    # Retrieve and display all records
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()

    conn.close()

    if not records:
        return "Table 'person_info' exists, but it does not contain any records."

    result = f"Table 'person_info' exists, and it contains the following records:\n"

    for record in records:
        result += f"ID: {record[0]}\n"  # Include ID here
        result += f"First Name: {record[1]}\n"
        result += f"Last Name: {record[2]}\n"
        result += f"Gender: {record[3]}\n"
        result += f"Age: {record[4]}\n"
        result += f"Birth Date: {record[5]}\n"
        result += f"Precinct Number: {record[6]}\n"
        result += f"Sector: {record[7]}\n"
        result += f"Organization: {record[8]}\n"
        result += f"Civil Status: {record[9]}\n\n"  # Adjust the index for Civil Status

    return result

# Specify the path to your database file
database_path = "my_database.db"

# Call the check_data function and print the result
result = check_data(database_path)
print(result)
