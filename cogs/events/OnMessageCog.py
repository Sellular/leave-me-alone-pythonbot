import discord
from discord.ext import commands

from utils import GeneralUtils

class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.mentions:
            if not message.author.bot:
                try:
                    userLeftAloneConfig = GeneralUtils.getConfig('userleftalone')

                    if not userLeftAloneConfig:
                        raise Exception("userleftalone section not found in config.")

                    userID = userLeftAloneConfig['user_id']
                    if not userID:
                        raise Exception("USER_ID not found in userleftalone config.")

                    leftAloneUser = discord.utils.get(message.guild.members, id = int(userID))
                    if not leftAloneUser:
                        raise Exception(f"User with id: {userID} not found in the guild.")

                    mentioned_user = False
                    for member in message.mentions:
                        if member.id == int(userID):
                            mentioned_user = True

                    if mentioned_user:
                        await message.channel.send(f"{message.author.mention} Please don't ping {leftAloneUser.display_name} unless it is important.")

                except Exception as error:
                    print(error)

def setup(bot: commands.Bot):
    bot.add_cog(OnMessageCog(bot))