import mysql.connector

def create_alx_book_store_db():
    db_config = {
        'host': 'localhost',  # Replace with your MySQL host
        'user': 'your_user',  # Replace with your MySQL username
        'password': 'your_password' # Replace with your MySQL password
    }

    try:
        # Establish a connection to the MySQL server
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # SQL statement to create the database if it doesn't exist
        sql_create_db = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the SQL statement
        cursor.execute(sql_create_db)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print(f"Error: Could not connect to MySQL server at {db_config['host']}. Please ensure the server is running and accessible.")
        else:
            print(f"Error: Failed to connect to DB: {err}")
    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'cnx' in locals() and cnx is not None:
            cnx.close()

if __name__ == "__main__":
    create_alx_book_store_db()