# Start of Discord Bot Development. арврврврававррав
![image](https://github.com/AndreMuhamed/Pogadon/assets/128980327/879275f3-3b5b-4751-a5a1-495456a16d8d)

![Untitled-1](https://github.com/AndreMuhamed/pogadon/assets/128980327/23b64a91-e2c1-47cf-aeae-144db6563c08)

***To create your first Discord bot, you need to follow these steps:*** 

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
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user}')

@bot.slash_command(description="Приветствие пользователя")
async def приветствие(ctx: disnake.ApplicationCommandInteraction):
    await ctx.response.send_message("Приветствую! Я готов помочь вам.")

@bot.slash_command(description="Поддержите наш проект донатом")
async def донат(ctx: disnake.ApplicationCommandInteraction):
    # Ваши ссылки на донат
    patreon_link = "https://www.patreon.com/andremuhamad"
    donationalerts_link = "https://www.donationalerts.com/r/andremuhamad"

    # Отправляем сообщение с ссылками на донат
    await ctx.send(content=f"**Поддержите наш проект донатом:**\nↈ {donationalerts_link}\nↈ {patreon_link}")

@bot.slash_command(description="Приглашение к оценке сервера")
async def прокачка(ctx: disnake.ApplicationCommandInteraction):
    # Ваше сообщение с приглашением к оценке сервера
    message = "Дайте оценку нашему серверу, если не сложно:\n\n" \
              "※ DiscordServer.Info: https://discordserver.info/1195867892063940671\n" \
              "※ ServerDiscord: https://server-discord.com/1195867892063940671"

    # Отправляем сообщение в текстовый канал
    await ctx.send(content=message)

@bot.slash_command(description="Приглашение к социальным сетям")
async def соцсеть(ctx: disnake.ApplicationCommandInteraction):
    # Ваша ссылка на социальные сети
    social_media_link = "https://bit.ly/3Px7sCH"

    # Отправляем сообщение с ссылкой
    await ctx.send(content=f"Присоединяйтесь к нашим сообществам в социальных сетях:\n{social_media_link}")

@bot.slash_command(description="Языки программирования")
async def язык_программирования(ctx: disnake.ApplicationCommandInteraction):
    await ctx.response.send_message("Мы поддерживаем множество языков программирования, включая Python, JavaScript, Java, C++ и другие.")
    
bot.run("YOUR_TOKEN")

```

You will also need to install the discord.py library if you haven't already, using the command `pip install discord.py`.

After writing the code, save it in a file with the extension `.py`, for example, `bot.py`.

*Step 4: Run the bot.*
Run your bot by executing the `bot.py` file from the command line or deploying it on a hosting server. Once the bot is running, you should see the message "Logged in as..." in the console.

# Now, your Discord bot should be active on the server and ready to respond to commands and messages!
