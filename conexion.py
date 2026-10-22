import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def obtener_conexion():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

if __name__ == "__main__":
    try:
        conn = obtener_conexion()
        print("Conexión exitosa")
        conn.close()
    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")