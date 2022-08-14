import discord
from discord.ext import commands

from dao import IgnoreRoleDAO

class IgnoreRoleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[839673797066096660], guild_only=True)
    @discord.option("role", discord.Role, description="Role to be ignored", required=True)
    async def ignorerole(self, ctx: discord.ApplicationContext, role: discord.Role):
        try:
            guild = role.guild

            if not guild:
                raise Exception("Guild not found.", ephemeral=True)

            IgnoreRoleDAO.insert(str(role.id), str(guild.id))
            await ctx.respond(f"{role.name}'s will be ignored.")
        except Exception as error:
            print(error)
            await ctx.respond("Error during ignoring role.", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(IgnoreRoleCog(bot))