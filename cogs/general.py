import discord
from discord.ext import commands


#Define Class
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Put Commands Below
    # 🆕 Manual sync command
    @discord.slash_command(name="sync", description="Manually sync application slash commands")
    async def sync(self, ctx: discord.ApplicationContext):

        has_admin_role = any(role.name == "Kamisama" for role in ctx.author.roles)

        if has_admin_role:
            await ctx.defer(ephemeral=True)
            await self.bot.sync_commands()
            await ctx.followup.send("✅ Bot synced!", ephemeral=True)
        else:
            await ctx.respond("🚫 You are not previledged to use this commands!", ephemeral=True)

#IMPORTANT!
#Add these to call the cog
def setup(bot):
    bot.add_cog(General(bot))