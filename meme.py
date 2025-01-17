import discord
from discord.ext import commands
import os

# Reemplaza esto con tu token de bot
TOKEN = 'token secreto'

# Ruta a la carpeta donde se encuentran las imágenes
CARPETA_IMAGENES = "./imagenes"  # La carpeta está en el mismo directorio que el script

# Intents necesarios
intents = discord.Intents.default()
intents.messages = True

# Configuración del bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def enviar_meme(ctx):
    """
    Comando para enviar la imagen 'meme1.jpeg' desde la carpeta 'imagenes'.
    Usa: !enviar_meme
    """
    nombre_imagen = "meme1.jpeg"
    ruta_completa = os.path.join(CARPETA_IMAGENES, nombre_imagen)

    # Verifica si la imagen existe
    if os.path.isfile(ruta_completa):
        try:
            with open(ruta_completa, 'rb') as img_file:
                await ctx.send(file=discord.File(img_file))
        except Exception as e:
            await ctx.send(f"Hubo un error al enviar la imagen: {e}")
    else:
        await ctx.send(f"No encontré la imagen `{nombre_imagen}` en la carpeta `imagenes`.")

# Inicia el bot
bot.run(TOKEN)
