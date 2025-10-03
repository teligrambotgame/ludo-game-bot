from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = "8037587323:AAHSp9yOOCEVL6bw2dpZtEiQ1Bjlxe-vMuo"

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Bot works!")

app.add_handler(CommandHandler("start", start))
app.run_polling()
