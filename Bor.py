import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from bots

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello! I am a bot!')

    await bot.process_commands(message)

@bot.command(name='hello')
async def say_hello(ctx):
    await ctx.send('Hello! I am a bot!')

bot.run('YOUR_BOT_TOKEN')
