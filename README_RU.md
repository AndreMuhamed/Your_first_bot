# Начало разработки Discord-бота.

_!Заказать Discord-бота: (https://t.me/admirall_times)!_

![Untitled-1](https://github.com/AndreMuhamed/pogadon/assets/128980327/23b64a91-e2c1-47cf-aeae-144db6563c08)

***Чтобы создать своего первого Discord-бота, выполните несколько шагов:***

*Шаг 1: Создание нового Discord-бота и получение токена бота.*
1. Перейдите на сайт разработчика Discord (https://discord.com/developers/applications).
2. Войдите в свою учетную запись или создайте новую.
3. Нажмите кнопку "New Application" (Новая программа) и введите название своего бота.

4. Перейдите на вкладку "Bot" (Бот) в меню слева.
5. Нажмите кнопку "Add Bot" (Добавить бота) и подтвердите создание бота.
6. В разделе "Token" (Токен) нажмите кнопку "Copy" (Скопировать) для сохранения токена бота. Обратите внимание, что этот токен должен храниться в тайне и не может быть размещен в открытом коде или отправлен кому-либо другому.

*Шаг 2: Приглашение бота на свой сервер Discord.*
1. Вернитесь на вкладку "General Information" (Общая информация) вашей программы.
2. Найдите ваш Client ID (идентификатор клиента) и скопируйте его.
3. Войдите на свой Discord-сервер и перейдите на вкладку "OAuth2" в настройках сервера.
4. В разделе "OAuth2 URL Generator" (Генератор URL для OAuth2) выберите опцию "bot".
5. Под опцией "Scopes" (Сферы) выберите "bot".
6. Под опцией "Bot Permissions" (Права бота) выберите необходимые права для своего бота (например, "Read Messages", "Send Messages" и т. д.).
7. Скопируйте сгенерированный URL-адрес OAuth2 и откройте его в веб-браузере.
8. Выберите сервер, на который вы хотите пригласить своего бота, и нажмите "Authorize" (Авторизовать).

*Шаг 3: Написание кода для бота.*
Вам нужно использовать библиотеку, которая предоставляет удобный интерфейс для работы с API Discord. Например, вы можете использовать библиотеку discord.py для Python.

Пример кода для базового бота на discord.py:

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
        return  # Игнорировать сообщения от ботов

    if message.content.lower().startswith('привет'):
        await message.channel.send('Привет! Я бот!')

    await bot.process_commands(message)

@bot.command(name='привет')
async def say_hello(ctx):
    await ctx.send('Привет! Я бот!')

bot.run('YOUR_BOT_TOKEN')
```

Вам также понадобится установить библиотеку discord.py, если она еще не установлена, с помощью команды `pip install discord.py`.

После написания кода сохраните его в файле с расширением `.py`, например, `bot.py`.

*Шаг 4: Запуск бота.*
Запустите своего бота, выполнив файл `bot.py` из командной строки или развернув его на хостинговом сервере. Когда бот будет запущен, вы увидите сообщение "Logged in as..." в консоли.

# Теперь ваш Discord-бот должен быть активным на сервере и готов отвечать на команды и сообщения!
