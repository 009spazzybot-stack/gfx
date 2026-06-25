import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(
        f"Logged in as {bot.user}"
    )

    await bot.tree.sync()


@bot.tree.command(
    name="ping",
    description="Bot latency"
)
async def ping(interaction):
    await interaction.response.send_message(
        f"Pong {round(bot.latency*1000)}ms"
    )


bot.run(TOKEN)
