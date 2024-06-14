import mysql.connector

# Conexión al servidor de base de datos (sin especificar una base de datos específica)
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

# Crear cursor
cursor1 = conexion1.cursor()

# Ejecutar una instrucción SQL para mostrar las bases de datos en el servidor
cursor1.execute("SHOW DATABASES")

# Imprimir el nombre de cada base de datos
for base in cursor1:
    print(base)

# Cerrar la conexión
conexion1.close()
