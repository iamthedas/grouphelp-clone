from telegram.ext import CommandHandler

def settings(update, context):
    update.message.reply_text('Settings menu coming soon.')

settings_handler = CommandHandler('settings', settings)