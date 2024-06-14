import mysql.connector
from mysql.connector import Error

try:
    # Conexión a la base de datos
    conexion1 = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db_users"
    )

    # Crear cursor
    cursor1 = conexion1.cursor()

    # Ejecutar una instrucción SQL para eliminar un registro específico de la tabla 'users' donde 'id' es 1234567890
    cursor1.execute("DELETE FROM users WHERE id=1234567890")

    # Confirmar los cambios en la base de datos
    conexion1.commit()

    # Ejecutar una instrucción SQL para seleccionar y mostrar todos los registros de la tabla 'users'
    cursor1.execute("SELECT id, name, rol FROM users")

    # Imprimir cada fila de resultados
    for fila in cursor1:
        print(fila)

except Error as e:
    print(f"Error: {e}")

finally:
    # Cerrar la conexión
    if conexion1.is_connected():
        cursor1.close()
        conexion1.close()
