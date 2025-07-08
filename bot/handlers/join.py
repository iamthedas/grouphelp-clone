from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ChatMemberHandler, ContextTypes

def welcome_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📂 Open Media", callback_data="alert:You must share this group first!")],
        [InlineKeyboardButton("🔗 Share Group", url="https://t.me/share/url?url=https://t.me/YourGroup")]
    ])

async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new = update.chat_member.new_chat_member
    if new.status == "member":
        name = new.user.mention_html()
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=f"👋 Welcome {name}! Please check the rules and share the group.",
            parse_mode="HTML",
            reply_markup=welcome_buttons()
        )

join_handler = ChatMemberHandler(send_welcome, ChatMemberHandler.CHAT_MEMBER)