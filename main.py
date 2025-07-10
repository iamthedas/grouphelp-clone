import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from bot.handlers.start import start_handler
from bot.handlers.join import join_handler
from bot.handlers.buttons import button_handler
from bot.handlers.settings import settings_handler

# Load environment variables (from Railway or .env file)
load_dotenv()

# Read token
TOKEN = os.environ.get("TG_BOT_TOKEN")
print(f"DEBUG_TOKEN: {repr(TOKEN)}")  # For logs

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
