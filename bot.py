import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('ODQzNDU4ODE2NTAxODc0NzM4.YKEKPA.-gyUZgCofyhTcY0phPEpLK2pbQQ')
