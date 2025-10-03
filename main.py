import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging enable karte hain
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Welcome to Ludo Game Bot! \nType /play to start playing.")

# Play command function
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Game Start hone wala hai... (Abhi basic test mode me hai)")

# Main function
def main():
    # Yahan apna bot token daalo (BotFather se jo mila hai)
    TOKEN = "8037587323:AAHSp9yOOCEVL6bw2dpZtEiQ1Bjlxe-vMuo"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
