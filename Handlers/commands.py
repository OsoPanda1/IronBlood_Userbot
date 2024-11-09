async def start(client, message):
    await message.reply("¡Hola! Soy tu bot de Telegram. Escribe /help para ver los comandos disponibles.")

async def help_command(client, message, comandos):
    mensaje_ayuda = "**Comandos disponibles:**\n"
    for comando, descripcion in comandos.items():
        mensaje_ayuda += f"- {comando}: {descripcion}\n"
    await message.reply(mensaje_ayuda)

async def father(client, message):
    await message.reply("SkyNet Userbot, soy una red de datos creada por [#ELTERRORDETELEGRAM]. Mi padre es Anubis Villaseñor {@Mrs_Anubis} Naci el 8/11/2024. Mi propósito es dejar Huella entre los demás bots.")