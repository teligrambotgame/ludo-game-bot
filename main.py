from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8037587323:AAHSp9yOOCEVL6bw2dpZtEiQ1Bjlxe-vMuo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Welcome to Ludo Game. Type /play to start the game."
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ludo game logic will start here. 🎲"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))

print("Bot is running...")
app.run_polling()
