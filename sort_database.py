import sqlite3

def sort_data(key_name):

    # Connect to the SQLite database (replace 'my_database.db' with your database file)
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all columns except 'id' and sort by the specified key
    cursor.execute(f"SELECT first_name,"
                   f"last_name,"
                   f"gender, "
                   f"age, birth_date, "
                   f"precinct_number, "
                   f"sector, "
                   f"organization, "
                   f"civil_status, "
                   f"house_number "
                   f"FROM person_info ORDER BY {key_name}")

    # Fetch the sorted data
    sorted_data = cursor.fetchall()

    # Close the database connection when you're done
    conn.close()

    # Convert the fetched data into a list of lists
    sorted_data_list = [list(record) for record in sorted_data]

    return sorted_data_list





