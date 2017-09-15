"""card-py-bot Discord bot api"""

from logging import getLogger

from discord.ext import commands

from card_py_bot.config import save_emoji_config, EMOJI_CONFIG_STRING
from card_py_bot.scrape import scrape_card, card_embed

DESCRIPTION = """card-py-bot: An WOTC Magic card link embedding Discord bot!"""

BOT = commands.Bot(command_prefix="?", description=DESCRIPTION)

__log__ = getLogger(__name__)


@BOT.event
async def on_ready():
    """Startup logged callout/setup"""
    __log__.info("logged in as: {}".format(BOT.user.id))


@BOT.event
async def on_message(message):
    """Standard message handler with card and shush functions"""
    if "http://gatherer.wizards.com/Pages/Card" in message.content:
        card_data = scrape_card(message.content)
        card_em = card_embed(card_data, message.content, BOT.user.avatar_url)
        await BOT.send_message(message.channel, embed=card_em)
    await BOT.process_commands(message)



class config():
    """Config commands for the card-py-bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def print_setup(self):
        """Print the emoji config strings for setting up the mana icon config"""
        await self.bot.say(EMOJI_CONFIG_STRING)

    @commands.command(pass_context=True)
    async def save_setup(self, ctx):
        """Save any user printed emoji config strings to the card_py_bot"""
        async for message in self.bot.logs_from(ctx.message.channel, limit=1):
            emoji_ids = \
                [emoji_id.lstrip("\\\\")
                 for emoji_id in message.content.split()[1:]]

            # Save the emoji ids into the emoji_config.json
            save_emoji_config(emoji_ids)


BOT.add_cog(config(BOT))