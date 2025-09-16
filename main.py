import discord
from discord import app_commands
import asyncio

class BotMaro(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"Bot {self.user} foi iniciado com sucesso")

bot = BotMaro()

@bot.tree.command(name="ola",description="primeiro comando do bot")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}")






await bot.start("token do bot")
