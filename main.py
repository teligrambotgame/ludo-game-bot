from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

BOT_TOKEN = "8037587323:AAHSp9yOOCEVL6bw2dpZtEiQ1Bjlxe-vMuo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot chal raha hai! Type /play to start Ludo.")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Ludo game start placeholder.")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))

print("Bot running... Type /start in Telegram")
app.run_polling()
