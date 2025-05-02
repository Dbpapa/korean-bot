import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "your_bot_token_here"

def load_dramas():
    with open("dramas.json", "r", encoding="utf-8") as f:
        return json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /drama <name> to search for a drama.")

async def drama(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please enter a drama name. Usage: /drama <name>")
        return

    query = ' '.join(context.args).lower()
    dramas = load_dramas()
    
    for drama in dramas:
        if query in drama["title"].lower():
            msg = (
                f"**Title:** {drama['title']}\n"
                f"**Country:** {drama['country']}\n"
                f"**Year:** {drama['year']}\n"
                f"**Rating:** {drama['rating']}\n"
                f"**Summary:** {drama['summary']}"
            )
            await update.message.reply_text(msg)
            return
    
    await update.message.reply_text("Drama not found in the database.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("drama", drama))
    app.run_polling()

if __name__ == "__main__":
    main()
