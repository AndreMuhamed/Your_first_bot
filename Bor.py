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
