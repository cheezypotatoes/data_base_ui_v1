import sqlite3

def insert_person_data(first_name, last_name, gender, age, birth_date, precinct_number, sector, organization, civil_status, house_number):
    # Connect to the SQLite database (or create one if it doesn't exist)
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Insert the new record
    insert_query = '''
    INSERT INTO person_info
    (first_name, last_name, gender, age, birth_date, precinct_number, sector, organization, civil_status, house_number)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_query,
                   (first_name, last_name, gender, age, birth_date, precinct_number, sector, organization, civil_status, house_number))
    conn.commit()
    conn.close()
