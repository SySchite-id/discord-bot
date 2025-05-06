import discord
from discord.ext import commands
import re

#Define Class
class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Put Commands Below
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        
        audio_file_path = "media/audio/hud-bang.mp3"
        if re.search(r'\bduar\b', message.content, re.IGNORECASE):
            try:
                await message.channel.send(file=discord.File(audio_file_path))
            except FileNotFoundError:
                await message.channel.send("kemem")

        if re.search(r'\bv\b', message.content, re.IGNORECASE):
            await message.channel.send(f"Panggilan kepada jenderal untuk memenuhi panggilan party @here")

#IMPORTANT!
#Add these to call the cog
def setup(bot):
    bot.add_cog(Tags(bot))