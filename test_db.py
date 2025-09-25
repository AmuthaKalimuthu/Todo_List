import pymysql

def test_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',  # Change this to your MySQL password
            database='todo_db'
        )
        print("MySQL connection successful!")
        connection.close()
        return True
    except Exception as e:
        print(f"MySQL connection failed: {e}")
        print("\n🔧 Fix options:")
        print("1. Make sure MySQL is running")
        print("2. Check username/password in config.py")
        print("3. Create database: CREATE DATABASE todo_db;")
        return False

if __name__ == '__main__':
    test_connection()