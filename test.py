import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",    # Change if needed
    user="root",         # Your MySQL username
    password="Deadpool17!",  # Your MySQL password
    database="Skinsense_Database"   # Your database name (optional)
)

if conn.is_connected():
    print("Connected to MySQL successfully!")

# Close the connection
conn.close()
