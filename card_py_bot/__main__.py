""" main argparse script entry point for the card-py-bot """

import argparse
import logging
import logging.handlers
import sys

from card_py_bot.card_bot import BOT


def main():
    """ main argparse startup script for the card-py-bot """
    parser = argparse.ArgumentParser(description="card-py-bot: a Discord bot "
                                                 "that web scrapes Magic card "
                                                 "links and embeds the "
                                                 "card's details into a "
                                                 "discord message")
    parser.add_argument("-t", "--token", type=str, required=True,
                        help="Discord Token for the bot")

    group = parser.add_argument_group(title="LOGGING")
    group.add_argument("-v", "--verbose", action="store_true",
                       help="Enable verbose logging")
    group.add_argument("-f", "--log-dir", dest="logdir",
                       help="Enable time rotating file logging, logging to "
                            "the path specified")
    group.add_argument("-d", "--debug", action="store_true",
                       help="Set the logging level to DEBUG")
    args = parser.parse_args()

    # initialize logging
    handlers = list()
    # handlers.append(logging.handlers.SysLogHandler(address="/dev/log"))

    if args.logdir is not None:
        handlers.append(
            logging.handlers.TimedRotatingFileHandler(
                args.logdir,
                when="D",
                interval=1,
                backupCount=45
            )
        )
    if args.verbose:
        handlers.append(logging.StreamHandler())

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=handlers
    )

    # run the bot
    BOT.run(args.token)

    return 0


if __name__ == "__main__":
    sys.exit(main())
