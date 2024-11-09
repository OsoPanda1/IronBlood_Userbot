import sqlite3
from pyrogram import Client, filters
from langdetect import detect
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.commands import start, help_command, father
from handlers.messages import handle_message
from utils.database import check_ban

# Crear el cliente de Pyrogram
app = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Diccionario para almacenar los comandos y sus descripciones
comandos = {
    "/start": "Inicia una conversación con el bot.",
    "/help": "Muestra esta ayuda.",
    "/father": "Conoce al creador del bot."
}

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await start(client, message)

@app.on_message(filters.command("help"))
async def help_handler(client, message):
    await help_command(client, message, comandos)

@app.on_message(filters.command("father"))
async def father_handler(client, message):
    await father(client, message)

@app.on_message(filters.text)
async def message_handler(client, message):
    await handle_message(client, message)

# Ejecutar el bot
app.run()