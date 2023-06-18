import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

image_chances = {
    'kot1.jpeg': 0.4,
    'kot2.jpeg': 0.7,
    'kot3.jpeg': 1.0,
    'mem1.jpeg': 0.6,
    'mem2.jpeg': 0.9,
    'mem3.jpeg': 0.1
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    animals = os.listdir('animals')
    img_name1 = random.choice(animals)
    with open(f'images/{img_name1}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run("token")
