import discord
from discord.ext import commands
import os
import json
import re

TRIGGER_FILE = "triggers.json"

#Define Class
class Triggers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.triggers = self.load_triggers()

    def load_triggers(self):
        if not os.path.exists(TRIGGER_FILE):
            with open(TRIGGER_FILE, 'w') as f:
                json.dump({}, f)
        with open(TRIGGER_FILE, 'r') as f:
            return json.load(f)
        
    def save_triggers(self):
        with open(TRIGGER_FILE, 'w') as f:
            json.dump(self.triggers, f, indent=4)

    #Put Commands Below
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        msg_content = message.content.lower()
        for keyword, response in self.triggers.items():
            if keyword in msg_content:
                await message.channel.send(response)
                break

        audio_file_path = "media/audio/hud-bang.mp3"
        if re.search(r'\bduar\b', message.content, re.IGNORECASE):
            try:
                await message.channel.send(file=discord.File(audio_file_path))
            except FileNotFoundError:
                await message.channel.send("kemem")
        
    @discord.slash_command(name="trigger_add", description="Add Trigger for auto response")
    async def trigger_add(self, ctx, keyword:str, response:str):
        has_admin_role = any(role.name == "Kamisama" for role in ctx.author.roles)

        if has_admin_role:
            self.triggers[keyword] = response
            self.save_triggers()
            await ctx.respond(f"✅ Trigger for `{keyword}` added.", ephemeral=True)
        else:
            await ctx.respond("🚫 You are not previledged to use this commands!", ephemeral=True)

    @discord.slash_command(name="trigger_remove", description="Remove an existing keyword trigger")
    async def trigger_remove(self, ctx, keyword: str):
        has_admin_role = any(role.name == "Kamisama" for role in ctx.author.roles)

        if has_admin_role:
            if keyword in self.triggers:
                del self.triggers[keyword]
                self.save_triggers()
                await ctx.respond(f"🗑️ Trigger `{keyword}` removed.", ephemeral=True)
            else:
                await ctx.respond("❌ That trigger doesn't exist.", ephemeral=True)
        else:
            await ctx.respond("🚫 You are not previledged to use this commands!", ephemeral=True)

    @discord.slash_command(name="trigger_list", description="List all triggers")
    async def trigger_list(self, ctx):
            if not self.triggers:
                await ctx.respond("No triggers set.", ephemeral=True)
            else:
                formatted = "\n".join([f"`{k}` ➜ {v}" for k, v in self.triggers.items()])
                await ctx.respond(f"📃 **Trigger List**:\n{formatted}", ephemeral=True)   

#IMPORTANT!
#Add these to call the cog
def setup(bot):
    bot.add_cog(Triggers(bot))