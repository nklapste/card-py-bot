"""card-py-bot Discord bot api"""

from logging import getLogger
import os

from discord.ext import commands

from card_py_bot import BASEDIR
from card_py_bot.config_emoji import print_ids
from card_py_bot.get_card import scrape_wizzards, card_embed


DESCRIPTION = """card-py-bot: An auto WOTC Magic card link parsing
and embedding Discord bot!"""

BOT = commands.Bot(command_prefix="?", description=DESCRIPTION)

__log__ = getLogger(__name__)


@BOT.event
async def on_ready():
    """Startup logged callout/setup"""
    __log__.info("logged in as: {}".format(BOT.user.id))


@BOT.event
async def on_message(message):
    """ Standard message handler with card and shush functions """
    if "http://gatherer.wizards.com/Pages/Card" in message.content:
        card_data = scrape_wizzards(message.content)
        card_em = card_embed(card_data, message.content, BOT.user.avatar_url)
        await BOT.send_message(message.channel, embed=card_em)
    await BOT.process_commands(message)


@BOT.command()
async def print_setup():
    """Print the emoji config strings for setting up the mana icon config"""
    await BOT.say(print_ids())


@BOT.command(pass_context=True)
async def save_setup(ctx):
    """Save any user printed emoji config strings to the card_py_bot"""
    async for message in BOT.logs_from(ctx.message.channel, limit=1):
        config_f = open(os.path.join(BASEDIR, "mana_config.txt"), "w")
        emoji_ids =\
            [emoji_id.lstrip("\\\\")
             for emoji_id in message.content.split()[1:]]

        for emoji_id in emoji_ids:
            config_f.write(emoji_id+"\n")
        config_f.close()

        __log__.info("Following emoji IDs were saved: {}".format(emoji_ids))

