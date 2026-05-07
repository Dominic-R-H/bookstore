import pymysql
import sqlite3

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="bookuser",
        password="password123",
        database="bookstore",
        cursorclass=pymysql.cursors.DictCursor
    )

    
