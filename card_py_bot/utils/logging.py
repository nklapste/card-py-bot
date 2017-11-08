"""General logging initilization for argparse"""

import logging
import logging.handlers


def add_logging_config(parser):
    """Add logging argparse arguments to a existing parser"""
    group = parser.add_argument_group(title="Logging config")
    group.add_argument("-v", "--verbose", action="store_true",
                       help="Enable verbose logging")
    group.add_argument("-f", "--log-dir", dest="logdir",
                       help="Enable time rotating file logging at "
                            "the path specified")
    group.add_argument("-d", "--debug", action="store_true",
                       help="Enable DEBUG logging level")


def config_logging(args):
    """From an argparse args dictionary initialize logging"""
    # initialize logging
    handlers = list()
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
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=handlers,
    )


