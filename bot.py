# bot.py
import discord
import random
import asyncio
import ffmpeg

from speech import convertToAudio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

from discord import FFmpegPCMAudio
from discord.utils import get

from settings import TOKEN, GUILD, COMMAND

bot = commands.Bot(command_prefix=COMMAND)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='talk', help='Convert text to audio and say it in voice channel, please write your sentence between quotes')
async def textToTalk(ctx, text):
    # Convertie le texte passé en paramètre, fonction de speech.py
    convertToAudio(text)
    # Se connecte au channel de l'expéditeur du message et lis le fichier créé précedemment
    try:
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="./ffmpeg/bin/ffmpeg.exe", source="output.mp3"))
    except:
        await ctx.send("You are not connected to a voice channel")
    
bot.run(TOKEN)