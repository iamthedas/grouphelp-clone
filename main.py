import os
from telegram.ext import ApplicationBuilder
from bot.handlers.start import start_handler
from bot.handlers.join import join_handler
from bot.handlers.buttons import button_handler
from bot.handlers.settings import settings_handler

# Debug: Print ALL environment variables
print("🧪 ENVIRONMENT VARIABLES:")
for key, val in os.environ.items():
    print(f"{key} = {val}")

# Read token
TOKEN = os.environ.get("TG_BOT_TOKEN")
print(f"DEBUG_TOKEN: {repr(TOKEN)}")

def main():
    if not TOKEN:
        print("❌ ERROR: Token is missing or empty. Check Railway 》Variables")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(start_handler)
    app.add_handler(settings_handler)
    app.add_handler(join_handler)
    app.add_handler(button_handler)

    print("✅ Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
