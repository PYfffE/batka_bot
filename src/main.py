import discord
from discord.ext import commands
from config import settings
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
counter = 0

@bot.command()
async def members_ids(ctx):
    for member in ctx.guild.members:
        # Kawa 321358688432685059
        print(member.name, member.id)

@bot.command()
async def roles_ids(ctx):
    for role in ctx.guild.roles:
        # Marked 767705402572800041
        print(role.name, role.id)

@bot.command()
async def guilds_ids(ctx):
    for guild in bot.guilds:
        # CYДAPN 271238809776029696
        print(guild.name, guild.id)

@bot.command()
async def mark_kawa(ctx):
    kawa = ctx.guild.get_member(321358688432685059)
    await kawa.remove_roles(ctx.guild.get_role(767705402572800041))

@bot.command()
async def unmark_kawa(ctx):
    kawa = ctx.guild.get_member(321358688432685059)
    await kawa.remove_roles(ctx.guild.get_role(767705402572800041))

@bot.command()
async def print_roles(ctx):
    kawa = ctx.guild.get_member(321358688432685059)
    for role in kawa.roles:
        print(role.name)

@bot.command()
async def kawa_status(ctx):
    for member in ctx.guild.members:
        if member.id == 321358688432685059:
            await ctx.send(member.status)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    global counter
    if message.author.id == 321358688432685059:
        counter += 1
    if counter == 3:
        kawa = message.guild.get_member(321358688432685059)
        await kawa.remove_roles(message.guild.get_role(767705402572800041))
        counter = 0
    await bot.process_commands(message)

print('Mzacha gomosex')
bot.run(settings['token'])
