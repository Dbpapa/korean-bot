from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = '7688983267:AAFAz9b8GfUvI-Rtt7F-De-mRUBh6PS7AK8'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello, I am your bot!')

def main():
    """Start the bot."""
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
