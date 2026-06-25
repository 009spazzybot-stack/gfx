import discord
from discord.ext import commands
from openai import OpenAI
from config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)


AI_CHANNEL_ID = 123456789012345678  # change this


class AIChat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if message.channel.id != AI_CHANNEL_ID:
            return

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a Discord assistant.
Be friendly and human.
Don't sound like a bot.
If someone is rude, you can be slightly rude back,
but don't be toxic.
"""
                },
                {
                    "role": "user",
                    "content": message.content
                }
            ]
        )

        reply = response.choices[0].message.content

        await message.reply(reply)


async def setup(bot):
    await bot.add_cog(AIChat(bot))
