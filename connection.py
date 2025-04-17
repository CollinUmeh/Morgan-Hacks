import mysql.connector
import os

conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="Deadpool17!",
    database="Skinsense DB"
)

cursor = conn.cursor()

def convert_to_binary(filename):
    with open(filename, "rb") as file:
        return file.read()

image_folder = r"C:\Users\Alexp\OneDrive\Desktop\GitHub\Skinsense Project\Datasets\Ringworm images"

for filename in os.listdir(image_folder):
    file_path = os.path.join(image_folder,filename)

    if os.path.isfile(file_path):
        image_data = convert_to_binary(file_path)
        sql ="INSERT INTO images (imag_name, image_data) VALUES (%s, %s)"
        cursor.execute(sql,(filename,image_data))
        print(f"Inserted {filename}")


conn.commit()
cursor.close()
conn.close()

print("All images uploaded successfully!")
