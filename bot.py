import discord
from discord.ext import commands

from utils import DBUtils, GeneralUtils, SetupUtils

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self):
        print("Bot running with:")
        print("Username: ", self.user.name)
        print("User ID: ", self.user.id)
        print('-----')

try:
    DBUtils.checkTables()

    bot = MyClient()
    botConfig = GeneralUtils.getConfig('bot')

    if not botConfig:
        raise Exception("Bot config not found.")

    bot_token = botConfig['token']
    if not bot_token:
        raise Exception("TOKEN not found in Bot config")

    SetupUtils.importCogs(bot)
    bot.run(bot_token)
except (Exception) as error:
    print(error)