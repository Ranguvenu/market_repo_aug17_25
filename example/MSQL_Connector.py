import mysql.connector

# Replace the placeholders with your database credentials
db_config = {
    'host': 'your_host',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_database'
}

# Establish a connection
connection = mysql.connector.connect(**db_config)

try:
    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Example: Execute a SELECT query
    cursor.execute("SELECT * FROM your_table")
    result = cursor.fetchall()

    # Example: Insert data into the table
    insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
    data_to_insert = ('value1', 'value2')
    cursor.execute(insert_query, data_to_insert)

    # Commit the changes
    connection.commit()

finally:
    # Close the cursor and connection when done
    cursor.close()
    connection.close()
