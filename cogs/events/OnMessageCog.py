import discord
from discord.ext import commands

from utils import GeneralUtils
from dao import IgnoreRoleDAO, LeaveAloneMemberDAO

class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.mentions:
            if not message.author.bot:
                try:
                    ignore_roles = IgnoreRoleDAO.getIgnoreRolesByGuild(str(message.guild.id))
                    if ignore_roles is None:
                        raise Exception("Error during ignore role retrieval")

                    ignore = False
                    for roleIDStr in ignore_roles:
                        roleID = int(roleIDStr)
                        ignore_role = discord.utils.get(message.author.roles, id=roleID)
                        if ignore_role:
                            ignore = True

                    if not ignore:
                        leave_alone_members = LeaveAloneMemberDAO.getLeaveAloneMembersByGuild(str(message.guild.id))
                        if leave_alone_members is None:
                            raise Exception("Error during leave alone member retrieval")

                        mentioned_users = []
                        for member in message.mentions:
                            for memberIDStr in leave_alone_members:
                                if member.id == int(memberIDStr):
                                    mentioned_users.append(member)

                        if mentioned_users:
                            for user in mentioned_users:
                                await message.channel.send(f"{message.author.mention} Please don't ping {user.display_name} unless it is important.")

                except Exception as error:
                    print(error)

def setup(bot: commands.Bot):
    bot.add_cog(OnMessageCog(bot))