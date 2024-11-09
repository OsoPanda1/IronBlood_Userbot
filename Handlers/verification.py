from pyrogram import Client, filters
from database.db import log_message, check_ban

async def message_handler(client, message):
    user_id = message.from_user.id
    if check_ban(user_id):
        await message.reply("Estás baneado y no puedes enviar mensajes.")
        return
    log_message(user_id, message.text)

def register_message_handlers(app):
    app.add_handler(filters.text & ~filters.command, message_handler)