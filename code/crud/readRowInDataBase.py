import mysql.connector

# Conexión a la base de datos especificando el host, el usuario, la contraseña y la base de datos
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_users"
)

# Crear cursor
cursor1 = conexion1.cursor()

# Ejecutar una instrucción SQL para seleccionar datos de la tabla 'articulos'
cursor1.execute("SELECT id, name, rol FROM users")

# Imprimir cada fila de resultados
for fila in cursor1:
    print(fila)

# Cerrar la conexión
conexion1.close()
