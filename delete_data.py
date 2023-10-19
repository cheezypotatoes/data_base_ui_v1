import sqlite3

def deleting_data(name, category):
    conn = None  # Initialize the connection variable

    try:
        # Connect to the SQLite database (replace 'my_database.db' with your actual database file)
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # SQL command to delete data with a specific condition (using category and name as placeholders)
        delete_sql = f"DELETE FROM person_info WHERE {category} = ?"

        # Execute the SQL command with the provided name as a parameter
        cursor.execute(delete_sql, (name,))

        # Commit the changes to the database
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")
    finally:
        if conn is not None:
            conn.close()  # Close the database connection if it was established

