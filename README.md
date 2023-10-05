# Start of Discord Bot Development.

_!Order Discord Bot: (https://t.me/admirall_times)!_

![Untitled-1](https://github.com/AndreMuhamed/pogadon/assets/128980327/23b64a91-e2c1-47cf-aeae-144db6563c08)

***To create your first Discord bot, you need to follow these steps:*** рвоевоопво

*Step 1: Create a new Discord bot and obtain the bot token.*
1. Go to the Discord Developer website (https://discord.com/developers/applications).
2. Log in to your account or create a new one.
3. Click on "New Application" and enter the name of your bot.

4. Go to the "Bot" tab on the left-hand menu.
5. Click "Add Bot" and confirm to create the bot.
6. In the "Token" section, click "Copy" to save the bot token. Remember that this token should be kept secret and should not be shared publicly or with anyone else.

*Step 2: Invite the bot to your Discord server.*
1. Go back to the "General Information" tab of your application.
2. Find your Client ID and copy it.
3. Log in to your Discord server and go to the "OAuth2" tab in server settings.
4. In the "OAuth2 URL Generator" section, select the "bot" option.
5. Under "Scopes," choose "bot".
6. Under "Bot Permissions," select the necessary permissions for your bot (e.g., "Read Messages", "Send Messages", etc.).
7. Copy the generated OAuth2 URL and open it in a web browser.
8. Choose the server to which you want to invite your bot and click "Authorize".

*Step 3: Write the code for your bot.*
You need to use a library that provides a convenient interface to work with the Discord API. For example, you can use the discord.py library for Python.

Here's an example code for a basic bot using discord.py:

```python
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
```

You will also need to install the discord.py library if you haven't already, using the command `pip install discord.py`.

After writing the code, save it in a file with the extension `.py`, for example, `bot.py`.

*Step 4: Run the bot.*
Run your bot by executing the `bot.py` file from the command line or deploying it on a hosting server. Once the bot is running, you should see the message "Logged in as..." in the console.

# Now, your Discord bot should be active on the server and ready to respond to commands and messages!
