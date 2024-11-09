import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN
from handlers import commands, messages
from auth.auth import authenticate_user

# Configuración del logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! Soy tu bot de administración de grupos.')

def main():
    updater = Updater(TOKEN)

    # Obtener el dispatcher para registrar los manejadores
    dp = updater.dispatcher

    # Comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", commands.help_command))
    
    # Mensajes
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, messages.handle_text))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()