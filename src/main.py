import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

@bot.command()
async def kawa_status(ctx):
    for member in ctx.guild.members:
        if member.id == 321358688432685059:
            await ctx.send(member.status)

print('Batka is working')
bot.run(settings['token'])
