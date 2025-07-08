from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚙️ Settings menu will appear here soon.")

settings_handler = CommandHandler("settings", settings)