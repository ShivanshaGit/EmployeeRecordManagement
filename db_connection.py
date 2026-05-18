# ============================================
# db_connection.py
# Handles MySQL connection
# ============================================

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


def get_connection():
    """Create and return a MySQL connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"\n[ERROR] Could not connect to database: {e}")
        print("Make sure MySQL is running and credentials in config.py are correct.\n")
        return None