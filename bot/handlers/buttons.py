from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data.startswith("alert:"):
        await query.answer(query.data[6:], show_alert=True)

button_handler = CallbackQueryHandler(handle_button)