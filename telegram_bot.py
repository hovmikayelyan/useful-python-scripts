#!/usr/bin/env python3
# @author hovmikayelyan

# This script allows us to make a bot and use it in Telegram.
# Needs the token of your application.
#
# Main functionality of the bot, is >
# accepts a link, downloads it and send to the user
#
# If running the script, throws an error `there is no module '...' in your machine`, then run:
# pip install python-telegram-bot --upgrade
# pip install requests

# Thank you!

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""

from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import __version__ as TG_VER
import logging
import requests
import re
import os

TOKEN = ""

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send message on `/start`.

    Args:
        update (Update):an object which represents an incoming update.
        context (ContextTypes.DEFAULT_TYPE): convenience class to gather customizable types of the :class:`telegram.ext.CallbackContext`
            interface.
    """

    await update.message.reply_text(
        f"🎉 Greeting, {update.message.chat.first_name}!\n\
            Send me the URL of your file(jpg|jpeg|JPG|gif|GIF|doc|DOC|pdf|PDF|mp4|mp3|pptx) you want me to download and send.")


async def sender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    user = update.message.from_user

    logger.info(
        f"Message from {user.first_name}({user.id}) -> {update.message.text}")

    url = update.message.text
    matched = re.compile(
        r"^.*\.(jpg|jpeg|JPG|gif|GIF|doc|DOC|pdf|PDF|mp4|mp3|pptx)$")
    result = matched.search(url)

    r = requests.get(url, allow_redirects=True)

    document = open(f"file.{result.group(1)}", 'wb').write(r.content)
    document = open(f"file.{result.group(1)}", 'rb')

    await context.bot.send_document(chat_id=user.id, document=document)

    document.close()
    os.remove(f"file.{result.group(1)}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.Regex(r'.*'), sender))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
