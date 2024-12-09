import logging
import os
import sys
from rich.logging import RichHandler
from utils.pretty_cli_logger import print_error, print_info, print_warning

# Check if the directory exists
if not os.path.exists("logs"):
    # If the directory does not exist, create it
    os.makedirs("logs")

# Create a custom logger
logger = logging.getLogger(__name__)


LOG_DEFAULT_FORMAT = (
    "%(asctime)s [%(thread)d] \n %(levelname)-5s %(name)s - %(message)s"
)

# 2024-12-08 15:52:01,351 [134891708809344] ERROR utils.logger - error log
# LOG_DEFAULT_FORMAT = "%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s"

logging.basicConfig(format=LOG_DEFAULT_FORMAT, level=logging.DEBUG)


def generate_logger(path=None, level=logging.DEBUG, log_format=LOG_DEFAULT_FORMAT):
    """generate new logger"""
    if path is None:
        print_warning("No log path provided, using default")
        sys.exit(1)

    if path:
        log_handler = logging.FileHandler(path)
    else:
        log_handler = logging.StreamHandler()
    # set log level
    print_info("log level %s", level)
    log_handler.setLevel(level)
    # set log format
    formatter = logging.Formatter(log_format)
    log_handler.setFormatter(formatter)
    # add log handler to logger
    logger.addHandler(log_handler)


# Set the level of handlers
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    # Create handlers
    print_info("frozen")
    # dump_handler = logging.FileHandler("logs/.log")
    # console_handler.setLevel(logging.CRITICAL)
else:
    generate_logger(path="logs/info.log", level=logging.INFO)
    generate_logger(path="logs/warm.log", level=logging.WARNING)
    generate_logger(path="logs/error.log", level=logging.ERROR)
    logging.StreamHandler()
    # dump logger for check
    # dump_handler = logging.FileHandler("logs/dump.log")
    # dump_handler.setLevel(logging.DEBUG)
    # logger.addHandler(dump_handler)
    # Set the level of handlers
    # console_handler.setLevel(logging.DEBUG)
