import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def check_ban(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM baneados WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def ban_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO baneados (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def unban_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM baneados WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

def log_message(user_id, mensaje):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensajes (user_id, mensaje) VALUES (?, ?)", (user_id, mensaje))
    conn.commit()
    conn.close()