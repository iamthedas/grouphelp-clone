import os
from telegram.ext import ApplicationBuilder
from bot.handlers.start import start_handler
from bot.handlers.join import join_handler
from bot.handlers.buttons import button_handler
from bot.handlers.settings import settings_handler

# Load bot token from Railway variable
TOKEN = os.environ.get("TG_BOT_TOKEN")
print("DEBUG_TOKEN:", repr(TOKEN))  # Log token to verify it's not None or empty

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Register all handlers
    app.add_handler(start_handler)
    app.add_handler(settings_handler)
    app.add_handler(join_handler)
    app.add_handler(button_handler)

    print("Bot started")
    app.run_polling()

if __name__ == "__main__":  # ✅ Double underscores — MUST be exact
    main()
