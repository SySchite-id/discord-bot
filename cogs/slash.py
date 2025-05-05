import discord
from discord.ext import commands


#Define Class
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Put Commands Below
    @discord.slash_command(name="status", description="Display Bot Status")
    async def status(self, ctx: discord.ApplicationContext):
        await ctx.respond("Hey there! 👋 Manager is Online.")

    @discord.slash_command(name="adminsay", description="Admin only announcer")
    async def adminsay(self, ctx:discord.ApplicationContext, message: str):   

        has_admin_role = any(role.name == "Kamisama" for role in ctx.author.roles)

        if has_admin_role:
            await ctx.respond(f"{message}")
        else:
            await ctx.respond("🚫 You are not previledged to use this commands!", ephemeral=True)

    @discord.slash_command(name="ping", description="Check latency")
    async def ping(self, ctx=discord.ApplicationContext):
        latency = round(self.bot.latency * 1000)
        await ctx.respond(f"Handshake Complete! {latency}ms")

#IMPORTANT!
#Add these to call the cog
def setup(bot):
    bot.add_cog(Slash(bot))