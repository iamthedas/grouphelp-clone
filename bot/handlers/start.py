from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📂 Open Media", callback_data="alert:You must share this first!")],
        [InlineKeyboardButton("🔗 Share Group", url="https://t.me/share/url?url=https://t.me/YourGroup")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! Use the buttons below:",
        reply_markup=start_buttons()
    )

start_handler = CommandHandler("start", start)