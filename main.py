from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatMemberHandler, CallbackQueryHandler
import os

TOKEN = "8007873539:AAE86STXidvvMbE3Jqt-E-Y3541JQ5uti88"

WELCOME_MESSAGE = f"""👋 Welcome {{name}}!

Before you proceed, please make sure to read the rules and share the group ❤️
"""

BUTTONS = [
    [InlineKeyboardButton("📂 Open Media", callback_data="alert:You must share this group once to unlock media!")],
    [InlineKeyboardButton("🔗 Share Group", url="https://t.me/share/url?url=https://t.me/YourGroupLink")]
]

async def send_welcome(update: Update, context):
    new_member = update.chat_member.new_chat_member
    if new_member.status == "member":
        name = new_member.user.mention_html()
        text = WELCOME_MESSAGE.format(name=name)
        reply_markup = InlineKeyboardMarkup(BUTTONS)
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=text,
            parse_mode='HTML',
            reply_markup=reply_markup
        )

async def handle_button(update: Update, context):
    query = update.callback_query
    if query.data.startswith("alert:"):
        msg = query.data.split("alert:")[1]
        await query.answer(text=msg, show_alert=True)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(send_welcome, ChatMemberHandler.CHAT_MEMBER))
    app.add_handler(CallbackQueryHandler(handle_button))
    print("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
