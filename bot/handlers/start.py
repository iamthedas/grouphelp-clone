from telegram.ext import CommandHandler

def start(update, context):
    update.message.reply_text('Welcome!')

start_handler = CommandHandler('start', start)