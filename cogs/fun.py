import random

import discord
from discord.ext import commands

from utils import config


GUILD_ID = config.secrets["discord"]["guild_id"]


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # React with random chess emoji on ping
        if self.bot.user.mentioned_in(message):
            if message.mention_everyone:
                return
            chess_emojis = config.config["fun"]["chess_emojis"]
            emoji, id = random.choice(list(chess_emojis.items()))
            await message.add_reaction(f"<:{emoji}:{id}>")

        # Affirm the glory of osu!
        lower_content = message.content.lower()
        if "i love osu" in lower_content:
            await message.reply("Osu 😻")

        if random.randint(1,100) <= 10 and "oh lord" in lower_content:
            await message.reply('https://www.youtube.com/watch?v=YsoP6bjADic')

        # User-specific reactions
        special_users = config.config["fun"]["special_users"]
        if random.randint(1, 100) <= 15 and message.author.id in special_users:
            emoji_set = random.choice(special_users[message.author.id])
            if isinstance(emoji_set, list):
                # List of reactions
                for emoji in emoji_set:
                    await message.add_reaction(emoji)
            else:
                # Single reaction
                await message.add_reaction(emoji_set)



def setup(bot):
    bot.add_cog(Fun(bot))

