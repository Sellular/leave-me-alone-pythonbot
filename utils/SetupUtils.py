import os
from discord.ext import commands

def importCogs(bot: commands.Bot):
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension(f"cogs.commands.{cogName}")
            print(f"Loaded {cogName}")

    for filename in os.listdir("./cogs/events"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension(f"cogs.events.{cogName}")
            print(f"Loaded {cogName}")