import os
from telegram.ext import ApplicationBuilder
from bot.handlers.start import start_handler
from bot.handlers.join import join_handler
from bot.handlers.buttons import button_handler
from bot.handlers.settings import settings_handler

# Load token
TOKEN = os.environ.get("TG_BOT_TOKEN")
print("DEBUG_TOKEN:", repr(TOKEN))  # Show raw value from env

def main():
    if not TOKEN:
        print("❌ ERROR: Token is missing or empty. Check Railway → Variables.")
        return  # Exit before crashing

    try:
        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(start_handler)
        app.add_handler(settings_handler)
        app.add_handler(join_handler)
        app.add_handler(button_handler)

        print("✅ Bot started")
        app.run_polling()
    except Exception as e:
        print("❌ EXCEPTION:", str(e))

if __name__ == "__main__":
    main()
