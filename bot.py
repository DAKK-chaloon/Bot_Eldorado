# bot.py
import discord
import asyncio
import ffmpeg

from speech import convertToAudio
from dialog import sayToBot

from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

from discord import FFmpegPCMAudio
from discord.utils import get

from settings import TOKEN, GUILD, COMMAND

bot = commands.Bot(command_prefix=COMMAND)

@bot.event
async def on_ready():
    print(f'{bot.user.name} est connecté à Discord!')

@bot.command(name='talk', help='"Phrase à envoyer" - Le bot reçoit la phrase passé en argument et y répond.')
async def textToTalk(ctx, text):
    # Envoi au bot le text et génère sa réponse
    reply = sayToBot(text)
    # Convertie le texte passé en paramètre, fonction de speech.py
    convertToAudio(reply)
    # Se connecte au channel de l'expéditeur du message et lis le fichier créé précedemment
    try:
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="./ffmpeg/bin/ffmpeg.exe", source="output.wav"))
    except:
        await ctx.send("Vous n'êtes pas connecté à un salon vocal.")
    
bot.run(TOKEN)