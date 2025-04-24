import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# 🆕 Manual sync command
@bot.slash_command(name="sync", description="Manually sync slash commands")
async def sync(ctx: discord.ApplicationContext):

    has_admin_role = any(role.name == "Kamisama" for role in ctx.author.roles)

    if has_admin_role:
        await bot.sync_commands()
        await ctx.respond("✅ Bot synced!", ephemeral=True)
    else:
        await ctx.respond("🚫 You are not previledged to use this commands!", ephemeral=True)

#Prefix Command
@bot.command()
async def hello(ctx):
    await ctx.send("Hey there! I'm alive and listening 👋")

@bot.command()
async def valo(ctx):
    await ctx.send("Gamau! Kamu ~~IRENG~~ IRON!")

@bot.command()
async def repo(ctx):
    await ctx.send(file=discord.File("media/audio/hud-bang.mp3"))

# Slash command
@bot.slash_command(name="status", description="Display Bot Status")
async def status(ctx: discord.ApplicationContext):
    await ctx.respond("Hey there! 👋 Manager is Online.")

@bot.slash_command(name="p", description="Salam")
async def p(ctx:discord.ApplicationContext):
    await ctx.respond("Apa kau pa pe pa pe! Assalamualaikum bodo.")

@bot.slash_command(name="hello", description="Greet someone")
async def hello(
    ctx: discord.ApplicationContext,
    user: discord.User
):
    await ctx.respond(f"Halo teman {user.mention}! 👋 ")

@bot.slash_command(name="adminsay", description="Admin only announcer")
async def adminsay(ctx:discord.ApplicationContext, message: str):   

    has_admin_role = any(role.name == "Kamisama" for role in ctx.author.roles)

    if has_admin_role:
        await ctx.respond(f"{message}")
    else:
        await ctx.respond("🚫 You are not previledged to use this commands!", ephemeral=True)

# Event Reaction
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    content = message.content.lower()

    if "pewpew" in content:
        await message.channel.send(f"VALO MALAM INI SERU GA SIH")


#Start Bot
with open("secret_token", "r") as file:
    token = file.read().strip()

bot.run(token)