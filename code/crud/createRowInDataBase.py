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

# Definir la instrucción SQL
sql = "INSERT INTO users(id, name, rol) VALUES (%s, %s, %s)"

# Datos a insertar
datos = ("1234567890", "Raul Fernandez", "adm")

# Ejecutar la instrucción SQL con los datos
cursor1.execute(sql, datos)

# Confirmar los cambios en la base de datos
conexion1.commit()

# Cerrar la conexión
conexion1.close()
