import mysql.connector

# Conexión a la base de datos 'db_users' en el host local con el usuario 'root' y sin contraseña
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_users"
)

# Crear cursor para ejecutar las instrucciones SQL
cursor1 = conexion1.cursor()

# Ejecutar una instrucción SQL para actualizar el rol de un usuario con un id específico
cursor1.execute("UPDATE users SET rol='admin' WHERE id=1234567890")

# Confirmar los cambios en la base de datos
conexion1.commit()

# Ejecutar una instrucción SQL para seleccionar todos los usuarios y sus datos actualizados
cursor1.execute("SELECT id, name, rol FROM users")

# Imprimir cada fila de resultados
for fila in cursor1:
    print(fila)

# Cerrar la conexión a la base de datos
conexion1.close()
