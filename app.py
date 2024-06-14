from flask import Flask, request, jsonify, session
from flask_cors import CORS
from handler.crud import connect_db, read_users, read_user, delete_user, update_user_role, create_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app, supports_credentials=True)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    correo = data.get('correo')
    password = data.get('password')
    
    connection = connect_db(host="localhost", user="root", passwd="", database="db_users")
    user = read_user(connection, ["id", "name", "rol", "correo"], [{"correo": correo, "password": password}])
    
    if user:
        session['username'] = user['name']
        session['role'] = user['rol']
        return jsonify({"message": "Login successful", "username": user['name'], "rol": user['rol']})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    correo = data.get('correo')
    password = data.get('password')
    rol = data.get('rol')

    connection = connect_db(host="localhost", user="root", passwd="", database="db_users")
    create_user(connection, [{"name": name, "password": password, "rol": rol, "correo": correo}])
    
    return jsonify({"message": "User created successfully"})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('rol', None)
    return jsonify({"message": "Logout successful"})

if __name__ == "__main__":
    # Connect to the database
    connection = connect_db(host="localhost", user="root", passwd="", database="db_users")

    # Define the columns to select
    columns = ["id", "name", "rol", "password", "correo"]

    # Perform operations
    print(read_users(connection, columns))
    # read_user(connection, columns, [{"correo": "example@example.com", "password": "password"}])
    # delete_user(connection, [{"id": "1"}, {"id": "2"}])
    # update_user_role(connection, [{"id": "1", "rol": "admin"}, {"id": "2", "rol": "user"}])
    # create_user(connection, [{"name": "Raul Fernandez", "password": "password", "rol": "admin", "correo": "raul@example.com"},
    #                         {"name": "Juan Perez", "password": "password", "rol": "user", "correo": "juan@example.com"}])

    # Close the connection
    if connection.is_connected():
        connection.close()

    app.run(debug=True)
