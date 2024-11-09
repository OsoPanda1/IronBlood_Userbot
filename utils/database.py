import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS baneados (
            user_id INTEGER PRIMARY KEY
        )
    ''')
    
   