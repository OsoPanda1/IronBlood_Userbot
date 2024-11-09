from langdetect import detect
from utils.database import check_ban

async def handle_message(client, message):
    user_id = message.from_user.id
    if check_ban(user_id):
        await message.reply("¡Estás baneado!")
        return

    texto = message.text
    if verificar_palabras_prohibidas(texto):
        await message.reply("Mensaje no permitido.")
    else:
        # Aquí puedes agregar la lógica para procesar el mensaje normalmente
        idioma_original = detect(texto)
        await message.reply(f"Detectado idioma: {idioma_original}")

def verificar_palabras_prohibidas(texto):
    palabras_prohibidas = ["palabra1", "palabra2"]  # Lista de palabras prohibidas
    return any(palabra in texto for palabra in palabras_prohibidas)