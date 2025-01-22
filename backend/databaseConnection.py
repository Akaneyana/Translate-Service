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
        raise  # Optionally, you could log this error to a file

def register_user(first_name, last_name, password, email):
    """
    Registers a new user by inserting their details into the database.
    The password is hashed before being stored.
    
    Args:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        password (str): The plain text password to hash.
        email (str): The user's email address.
    """
    try:
        # Hash the password
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Establish the database connection
        db = get_connection()
        cursor = db.cursor()

        # Query to insert user data into the Users table
        query = """
            INSERT INTO Users (FirstName, LastName, Password_hash, Email)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, hashed_password, email))

        # Commit the transaction
        db.commit()

        print("User registered successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def save_reaction_time(user_id, reaction_time):
    """
    Save a reaction time score into the database.
    Args:
        user_id (int): The ID of the user (if applicable).
        reaction_time (float): The reaction time score in milliseconds.
    """
    try:
        db = get_connection()
        cursor = db.cursor()

        # Insert the reaction time into the ReactionTime table
        query = """
            INSERT INTO ReactionTime (User_id, Reaction_Time_ms)
            VALUES (%s, %s)
        """
        cursor.execute(query, (user_id, reaction_time))

        db.commit()
        print("Reaction time saved successfully!")
    except Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
