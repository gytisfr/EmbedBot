#EmbedBot by ~ Gytis5089

import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = 'embed ', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"embed help"))
    print('EmbedBot now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.command()
async def create(ctx, title, colour, *, message):
    if colour in ['red', 'Red']:
        finalcolour = 0xFF0000
    elif colour in ['blue', 'Blue']:
        finalcolour = 0x0000FF
    elif colour in ['yellow', 'Yellow']:
        finalcolour = 0xFFFF00
    elif colour in ['orange', 'Orange']:
        finalcolour = 0xFFA500
    elif colour in ['green', 'Green']:
        finalcolour = 0x00FF00
    elif colour in ['swamp', 'Swamp']:
        finalcolour = 0x001e17
    elif colour in ['aqua', 'Aqua']:
        finalcolour = 0x00FFFF
    elif colour in ['purple', 'Purple']:
        finalcolour = 0xFF00FF
    elif colour in ['black', 'Black']:
        finalcolour = 0x000000
    elif colour in ['white', 'White']:
        finalcolour = 0xFFFFFF
    elif colour in ['grey', 'Grey', 'gray', 'Gray']:
        finalcolour = 0xC0C0C0
    embed = discord.Embed(
        title=title,
        colour=finalcolour,
        description=message
    )
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        colour=0x7289DA,
        description="embed create `title` `colour` `message`\n\nFor help with available colours, run `embed colours`"
    )
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)

@client.command(aliases=['colour', 'colors', 'color'])
async def colours(ctx):
    embed = discord.Embed(
        title="Colours",
        colour=0x7289DA,
        description="Red, Blue, Yellow, Green, Swamp, Aqua, Purple, Black, White, Gray"
    )
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)

client.run('ODY3OTY5ODczMjk1MzM1NDk0.YPo17w.VNPBQlPBlv7nNHdbuK2lxL2nB5c')