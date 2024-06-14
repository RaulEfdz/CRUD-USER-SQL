import mysql.connector

# Conexión a la base de datos
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_users"
)

# Crear cursor
cursor1 = conexion1.cursor()

# Ejecutar una instrucción SQL para mostrar las tablas en la base de datos
cursor1.execute("SHOW TABLES")

# Imprimir el nombre de cada tabla
for tabla in cursor1:
    print(tabla)

# Cerrar la conexión
conexion1.close()
