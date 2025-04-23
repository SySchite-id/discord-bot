import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hey there! I'm alive and listening 👋")

@bot.command()
async def valo(ctx):
    await ctx.send("Gamau! Kamu ~~IRENG~~ IRON!")

@bot.command()
async def repo(ctx):
    await ctx.send(file=discord.File("media/audio/hud-bang.mp3"))

bot.run("MTM2NDQ3MDg2MDg4MjExNjYyOA.Gd9RWo.U9eTEvt9YBUW9pcBOUpFhP6MgVTmGk4VF_tUeU")