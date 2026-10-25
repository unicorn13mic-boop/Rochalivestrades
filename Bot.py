import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Rocha Lives Trades! 📈\n\n"
        "Your Telegram bot is online.\n\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/status - Check bot status\n"
        "/signals - Check signal status\n\n"
        "BTC 15-minute signals are not connected yet."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Rocha Lives Trades is running!\n"
        "Trading mode: Signals only\n"
        "Automatic trading: Disabled"
    )


async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 BTC 15-minute signals\n\n"
        "Signal feed: Not connected yet.\n"
        "No live UP or DOWN recommendation is available."
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN environment variable."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("signals", signals))

    print("Rocha Lives Trades bot is starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
