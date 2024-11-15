<div align="center">  
  <h1>🚀 Start of Discord Bot Development</h1>  
  <p>  
    Створіть свій перший Discord-бот за допомогою цього покрокового гайда!  
  </p>  
  <img src="https://github.com/AndreMuhamed/Pogadon/assets/128980327/879275f3-3b5b-4751-a5a1-495456a16d8d" alt="Discord Development" width="600"/>  
  <img src="https://github.com/AndreMuhamed/pogadon/assets/128980327/23b64a91-e2c1-47cf-aeae-144db6563c08" alt="Bot Features" width="600"/>  
</div>  

---

## 🎯 **Що це таке?**  
Це покроковий гайд зі створення вашого першого Discord-бота! Ви навчитесь:  
- 🔑 Створювати бота та отримувати токен.  
- ✨ Додавати бота на сервер.  
- 💻 Писати базовий код для роботи вашого бота.  

---

##🛠️ **Крок 1: Створення Discord-бота та отримання токена**


1. Перейдіть до [Discord Developer Portal](https://discord.com/developers/applications).  
2. Увійдіть до облікового запису або створіть новий.  
3. Натисніть **"New Application"** та введіть ім'я бота.  
4. У меню зліва перейдіть до розділу **"Bot"**.  
5. Натисніть **"Add Bot"** і підтвердьте дію.  
6. Скопіюйте **токен бота**. Збережіть його в надійному місці — це ваш ключ доступу!  

---

## 🌐 **Крок 2: Додавання бота на сервер** 

1. Перейдіть до вкладки **"OAuth2"** у вашій аплікації.  
2. У секції **"OAuth2 URL Generator"** оберіть:  
   - **Scopes:** `bot`  
   - **Permissions:** потрібні права для бота (наприклад, `Send Messages`).  
3. Скопіюйте згенероване посилання та відкрийте його у браузері.  
4. Виберіть сервер і натисніть **"Authorize"**.  

---

## 💻 **Крок 3: Написання коду бота**

Ваш код на Python із використанням бібліотеки `disnake`:  

```python
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f"Бот запущен як {bot.user}")

@bot.slash_command(description="Привітання користувача")
async def привіт(ctx: disnake.ApplicationCommandInteraction):
    await ctx.response.send_message("Привіт! Я готовий допомогти тобі.")

@bot.slash_command(description="Посилання на донати")
async def донат(ctx: disnake.ApplicationCommandInteraction):
    patreon = "https://www.patreon.com/andremuhamad"
    alerts = "https://www.donationalerts.com/r/andremuhamad"
    await ctx.send(f"**Підтримайте проект:**\n- {patreon}\n- {alerts}")

@bot.slash_command(description="Запрошення оцінити сервер")
async def оцінка(ctx: disnake.ApplicationCommandInteraction):
    feedback = (
        "※ [DiscordServer.Info](https://discordserver.info/1195867892063940671)\n"
        "※ [ServerDiscord](https://server-discord.com/1195867892063940671)"
    )
    await ctx.send(f"Залиште свою оцінку:\n{feedback}")

@bot.slash_command(description="Соціальні мережі")
async def соцмережі(ctx: disnake.ApplicationCommandInteraction):
    social = "https://bit.ly/3Px7sCH"
    await ctx.send(f"Долучайтесь до нас:\n{social}")

bot.run("YOUR_TOKEN")
```

---

## ▶️ **Крок 4: Запуск бота** 


1. Встановіть `disnake`, якщо ще цього не зробили:  
   ```bash
   pip install disnake
   ```  
2. Збережіть код у файл (наприклад, `bot.py`).  
3. Запустіть бот через термінал:  
   ```bash
   python bot.py
   ```  

---

## 📜 **Результат**
Ваш бот тепер активний на сервері! 🥳 Ви можете додавати нові команди та розширювати його функціонал. 

---

<div align="center">  
  <h2>🤝 Підтримка проекту</h2>  
</div>  

- Patreon: https://www.patreon.com/andremuhamad)  
- DonationAlerts: https://www.donationalerts.com/r/andremuhamad)  

> **Вдалого кодування!**
