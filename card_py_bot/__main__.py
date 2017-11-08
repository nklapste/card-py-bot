"""Main script entry point for the card-py-bot"""
import argparse
import sys

from card_py_bot.bot import BOT
import card_py_bot.config

from card_py_bot.utils.logging import add_logging_config, config_logging
def main():
    """Startup script for the card-py-bot"""
    parser = argparse.ArgumentParser(description="card-py-bot: a Discord bot "
                                                 "that web scrapes Magic card "
                                                 "links and embeds the "
                                                 "card's details into a "
                                                 "Discord message")

    parser.add_argument("-c", "--emoji-config-path", type=str,
                        default=card_py_bot.config.EMOJI_CONFIG_PATH,
                        dest="emoji_config_path",
                        help="Path to the card-py-bot emoji_config.json to be "
                             "loaded/generated from (default: %(default)s)")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--token", type=str,
                       help="String of the Discord token for the bot")
    group.add_argument("-tf", "--token-file", type=str, dest="token_file",
                       help="Path to file containing the Discord token for "
                            "the bot")

    add_logging_config(parser)
    args = parser.parse_args()
    config_logging(args)

    # set the emoji config path
    card_py_bot.config.EMOJI_CONFIG_PATH = args.emoji_config_path

    # read the token file and extract the token
    if args.token_file is not None:
        token_file = open(args.token_file, "r")
        token = str(token_file.read()).strip()
        token_file.close()
    elif args.token is not None:
        token = args.token
    # run the bot
    BOT.run(token)

    return 0


if __name__ == "__main__":
    sys.exit(main())
