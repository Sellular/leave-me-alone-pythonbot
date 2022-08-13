import discord
from discord.ext import commands

from utils import GeneralUtils, SetupUtils

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=("X$X$"), intents=intents)

    async def on_ready(self):
        SetupUtils.importCogs(self)
        print("Bot running with:")
        print("Username: ", self.user.name)
        print("User ID: ", self.user.id)
        print('-----')

try:
    bot = MyClient()
    botConfig = GeneralUtils.getConfig('bot')

    if not botConfig:
        raise Exception("Bot config not found.")

    bot_token = botConfig['token']
    if not bot_token:
        raise Exception("TOKEN not found in Bot config")

    bot.run(bot_token)
except (Exception) as error:
    print(error)