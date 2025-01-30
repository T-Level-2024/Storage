import mysql.connector

# Create a connection to the database
try:
    conn = mysql.connector.connect(
        host='localhost',  # Replace with your DB host
        user='root',       # Replace with your MySQL username
        password='',       # Replace with your MySQL password
        database='test_db'  # Replace with your database name
    )

    if conn.is_connected():
        print("Database Connected Successfully!")
        cursor = conn.cursor()
        command = ("SELECT * FROM testtable")
        result = ""
        cursor.execute(command)
        for(name, age, date_of_birth, subject, serial_number) in cursor:
            print(name, "|", date_of_birth, "|", subject)

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        conn.close()
