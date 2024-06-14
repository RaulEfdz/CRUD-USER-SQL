import mysql.connector
from mysql.connector import Error

def connect_db(host="localhost", user="root", passwd="", database="db_users"):
    """
    Establishes a connection to the database using provided credentials.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def read_users(connection, columns):
    """
    Reads and prints all users from the database, selecting specified columns.
    """
    if connection:
        cursor = connection.cursor()
        columns_str = ", ".join(columns)
        cursor.execute(f"SELECT {columns_str} FROM users")
        for row in cursor:
            print(row)
        cursor.close()

def read_user(connection, columns, conditions):
    """
    Reads and prints specific users from the database based on conditions, selecting specified columns.
    """
    if connection:
        cursor = connection.cursor()
        columns_str = ", ".join(columns)
        for condition in conditions:
            query = f"SELECT {columns_str} FROM users WHERE " + " AND ".join(f"{k}=%s" for k in condition.keys())
            values = tuple(condition.values())
            cursor.execute(query, values)
            for row in cursor:
                print(row)
        cursor.close()

def delete_user(connection, conditions):
    """
    Deletes specific users from the database based on conditions.
    """
    if connection:
        cursor = connection.cursor()
        for condition in conditions:
            query = "DELETE FROM users WHERE " + " AND ".join(f"{k}=%s" for k in condition.keys())
            values = tuple(condition.values())
            cursor.execute(query, values)
        connection.commit()
        cursor.close()

def update_user_role(connection, updates):
    """
    Updates the role of specific users in the database based on provided updates.
    """
    if connection:
        cursor = connection.cursor()
        for update in updates:
            id_value = update.pop("id")
            set_clause = ", ".join(f"{k}=%s" for k in update.keys())
            query = f"UPDATE users SET {set_clause} WHERE id=%s"
            values = tuple(update.values()) + (id_value,)
            cursor.execute(query, values)
        connection.commit()
        cursor.close()

def create_user(connection, users):
    """
    Creates new users in the database based on provided user data.
    """
    if connection:
        cursor = connection.cursor()
        for user in users:
            # Check if the user already exists
            query_check = "SELECT COUNT(*) FROM users WHERE id=%s"
            cursor.execute(query_check, (user['id'],))
            if cursor.fetchone()[0] == 0:
                columns = ", ".join(user.keys())
                placeholders = ", ".join("%s" for _ in user.values())
                query = f"INSERT INTO users ({columns}) VALUES ({placeholders})"
                values = tuple(user.values())
                cursor.execute(query, values)
        connection.commit()
        cursor.close()

# from handler.crud import connect_db, read_users, read_user, delete_user, update_user_role, create_user

# if __name__ == "__main__":
#     # Connect to the database
#     connection = connect_db(host="localhost", user="root", passwd="", database="db_users")

#     # Define the columns to select
#     columns = ["id", "name", "rol"]

#     # Perform operations
#     read_users(connection, columns)
#     read_user(connection, columns, [{"id": "1234567890"}])
#     delete_user(connection, [{"id": "1234567890"}, {"id": "1234567891"}])
#     update_user_role(connection, [{"id": "1234567890", "rol": "admin"}, {"id": "1234567891", "rol": "admin"}])
#     create_user(connection, [{"id": "1234567890", "name": "Raul Fernandez", "rol": "adm"}, {"id": "1234567891", "name": "Juan Perez", "rol": "user"}])

#     # Close the connection
#     if connection.is_connected():
#         connection.close()
