import mysql.connector
from mysql.connector import Error
import hashlib
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def get_connection():
    """
    Establish a connection to the database using parameters from the .env file.
    Returns:
        A MySQL database connection object.
    """
    try:
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_DATABASE")
        
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Error as err:
        print(f"Error connecting to the database: {err}")
        raise

def register_user(first_name, last_name, password, email):
    """
    Registers a new user in the database.
    """
    try:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        db = get_connection()
        cursor = db.cursor()

        query = """
            INSERT INTO Users (FirstName, LastName, Password_hash, Email)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, hashed_password, email))
        db.commit()
        print("User registered successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
            
            
def verify_user_credentials(email, password):
    try:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        db = get_connection()
        cursor = db.cursor()

        # Query to fetch the user ID and hashed password
        query = "SELECT User_id, Password_hash FROM Users WHERE Email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result and result[1] == hashed_password:
            return result[0]  # Return User_id
        return None
    except Error as err:
        print(f"Error verifying user credentials: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def place_order(user_id, Book, Language, Note):
    """
    Places an order in the Orders table for a given user.
    """
    try:
        db = get_connection()
        cursor = db.cursor()

        query = "INSERT INTO Orders (User_id, Book, Language, Note) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, Book, Language, Note))
        db.commit()
    except Error as err:
        raise Exception(f"Failed to place order: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
