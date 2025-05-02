import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load dramas from JSON
with open("dramas.json", "r", encoding="utf-8") as f:
    dramas = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me the name of a Korean or Chinese drama!")

async def search_drama(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    results = [d for d in dramas if query in d['title'].lower()]
    if results:
        reply = ""
        for drama in results:
            reply += f"**Title:** {drama['title']}\n"
            reply += f"**Type:** {drama['type']}\n"
            reply += f"**Year:** {drama['year']}\n"
            reply += f"**Description:** {drama['description']}\n\n"
        await update.message.reply_text(reply.strip(), parse_mode='Markdown')
    else:
        await update.message.reply_text("Drama not found. Try another name.")

if __name__ == "__main__":
    import os
    TOKEN = os.environ.get("BOT_TOKEN")  # Set BOT_TOKEN in Koyeb secret env
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("search", search_drama))  # Optional
    app.add_handler(CommandHandler("drama", search_drama))   # Optional
    app.add_handler(CommandHandler(None, search_drama))

    app.run_polling()
