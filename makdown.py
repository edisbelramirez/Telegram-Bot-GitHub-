import telegram
from telegram.ext import CommandHandler, Updater
import requests

# Configuración del bot de Telegram y token de GitHub
bot = telegram.Bot(token='TOKEN_DEL_BOT')
github_token = 'GITHUB_PERSONAL_ACCESS_TOKEN'

# Manejar el comando /leermd
def leer_md(update, context):
    # Llamada a la API de GitHub para obtener el contenido del archivo .md
    repo_owner = 'REPOSITORIO_PROPIETARIO'
    repo_name = 'NOMBRE_DEL_REPOSITORIO'
    file_path = 'RUTA_DEL_ARCHIVO.md'

    headers = {
        'Authorization': 'token ' + github_token
    }

    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    response = requests.get(url, headers=headers)
    content = response.json()['content']

    # Decodificar el contenido del archivo .md
    md_content = base64.b64decode(content).decode('utf-8')

    # Enviar el contenido decodificado al chat
    context.bot.send_message(chat_id=update.message.chat_id, text=md_content)

# Configurar el gestor de comandos para el bot
updater = Updater(token='TOKEN_DEL_BOT', use_context=True)
dispatcher = updater.dispatcher
leer_md_handler = CommandHandler('leermd', leer_md)
dispatcher.add_handler(leer_md_handler)

# Iniciar el bot
updater.start_polling()
updater.idle()
