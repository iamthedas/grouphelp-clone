from telegram.ext import MessageHandler, filters

def on_join(update, context):
    pass

join_handler = MessageHandler(filters.ALL, on_join)