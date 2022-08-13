import os
from discord.ext import commands

def importCogs(bot: commands.Bot):
    for filename in os.listdir("./cogs/events"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.events." + cogName)