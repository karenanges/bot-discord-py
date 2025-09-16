import discord
from discord import app_commands
import asyncio
import random 

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

@bot.tree.command(name="ola")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}")


@bot.tree.command(name="abraco")
@app_commands.describe(user="Escolha alguém para abraçar")
async def abraco(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f"{interaction.user.mention} deu um abraço em {user.mention} 🤗")

@bot.tree.command(name="soco")
@app_commands.describe(user="Dê um soco em alguém")
async def soco(interaction: discord.Interaction, user: discord.Member):
  await interaction.response.send_message(f"{interaction.user.mention} deu um soco em {user.mention}🤬👊")


@bot.tree.command(name="ship")
@app_commands.describe(user1="Primeira pessoa", user2="Segunda pessoa")
async def ship(interaction: discord.Interaction, user1: discord.Member, user2: discord.Member):
    
    porcentagem = random.randint(0, 100)

    
    if porcentagem > 80:
        msg = "💖 Perfeito! Esse casal tem química de sobra!"
    elif porcentagem > 50:
        msg = "💛 Pode dar certo, mas precisa de um pouco de esforço."
    elif porcentagem > 20:
        msg = "💔 Hmmm… vai ser complicado, cuidado!"
    else:
        msg = "💀 Desastre amoroso! Melhor não tentar."

    
    await interaction.response.send_message(
        f"{user1.mention} ❤️ {user2.mention}\nCompatibilidade: {porcentagem}%\n{msg}"
    )



await bot.start("token do bot")

