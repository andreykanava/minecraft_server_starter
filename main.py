import discord
from python_aternos import Client
from discord.ext import commands

discord = commands.Bot(command_prefix='!', intents = discord.Intents(messages = True, guild_messages = True, members = True, guilds = True, voice_states = True))
aternos = Client.from_credentials('', '')

@discord.command(aliases=["startserver", "ss", "start"])
async def start_server(ctx):
    try:
        servs = aternos.list_servers()
        myserv = servs[0]
        myserv.start()
        await  ctx.channel.send(content=":white_check_mark:Запускаю! Почекайте декілька хвилин:white_check_mark: ")
    except:
        await  ctx.channel.send(content=":white_check_mark:Сервер вже запущений!:white_check_mark: ")

discord.run("")
