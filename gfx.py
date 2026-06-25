import discord
from discord import app_commands
from discord.ext import commands


class GFX(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(
        name="poster",
        description="Create esports poster"
    )
    async def poster(
        self,
        interaction: discord.Interaction,
        player:str,
        team:str,
        color:str
    ):

        await interaction.response.send_message(
            f"""
Generating poster:

Player: {player}
Team: {team}
Theme: {color}

Searching assets...
"""
        )


async def setup(bot):
    await bot.add_cog(GFX(bot))
