import mysql.connector

def get_connection():
    try:
        con=mysql.connector.connect(host="localhost",user="root",password="Shreeram@123",database="library_db")
        
        if con.is_connected():
            return con
        
    except mysql.connector.Error as e:
        print("Database connection error:",e)
        
    return None