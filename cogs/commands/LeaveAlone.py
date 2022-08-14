import discord
from discord.ext import commands

from dao import LeaveAloneMemberDAO

class LeaveAloneCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    @discord.option("member", discord.Member, description="Member to leave alone", required=True)
    async def leavealone(self, ctx: discord.ApplicationContext, member: discord.Member):
        try:
            guild = member.guild

            if not guild:
                raise Exception("Guild not found.")

            LeaveAloneMemberDAO.insert(str(member.id), str(guild.id))
            await ctx.respond(f"{member.display_name} will now be left alone", ephemeral=True)
        except Exception as error:
            print(error)
            await ctx.respond("Error during leaving user alone.", ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(LeaveAloneCog(bot))