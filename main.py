import discord
from python_aternos import Client
from discord.ext import commands

discord = commands.Bot(command_prefix='!')
aternos = Client.from_credentials('Weyther', 'Qawe4r%tyu*i')

@discord.command(aliases=["startserver", "ss", "start"])
async def start_server(ctx):
    try:
        servs = aternos.list_servers()
        myserv = servs[0]
        myserv.start()
        await  ctx.channel.send(content=":white_check_mark:Запускаю! Почекайте декілька хвилин:white_check_mark: ")
    except:
        await  ctx.channel.send(content=":white_check_mark:Сервер вже запущений!:white_check_mark: ")

discord.run("MTAxMjA1NDAzMTk0Mzg3MjU1Mw.GRlTK8.JZ0DjFcwRC4feePrrv6R0U_qYmZYu01vihr5gk")
