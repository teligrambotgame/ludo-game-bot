import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Apna Bot Token yahan dalen
BOT_TOKEN = "8037587323:AAHSp9yOOCEVL6bw2dpZtEiQ1Bjlxe-vMuo"

# Players data
players = {"Player1": 0, "Player2": 0}
turn_order = ["Player1", "Player2"]
current_turn = 0

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 Welcome to Telegram Ludo!\nType /roll to roll the dice."
    )

# Roll dice
async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_turn
    player = turn_order[current_turn]
    dice = random.randint(1, 6)
    players[player] += dice

    msg = f"{player} rolled a {dice}!\nPosition: {players[player]}"

    if players[player] >= 20:  # Simple winning condition
        msg += f"\n🎉 {player} wins!"
        players["Player1"] = 0
        players["Player2"] = 0

    await update.message.reply_text(msg)

    current_turn = (current_turn + 1) % 2

# Setup bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("roll", roll))

print("Bot running... Type /start in Telegram")
app.run_polling()
