import sqlite3
from pyrogram import Client, filters
from handlers.commands import register_commands
from handlers.messages import register_message_handlers
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Inicializar la base de datos
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS baneados (
            user_id INTEGER PRIMARY KEY
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            mensaje TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("¡Hola! Soy tu bot de Telegram.")

# Registrar manejadores
register_commands(app)
register_message_handlers(app)

# Inicializar la base de datos
init_db()

# Ejecutar el bot
app.run()