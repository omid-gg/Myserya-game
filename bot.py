import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from flask import Flask, jsonify
import uvicorn
from bot import app  # اصلاح شده

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "سلام! خوش اومدی به بازی فانتزی! برای شروع بازی دستور 'play' رو بزن."
    )

def play(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "بازی شروع شد! آماده مبارزه هستید."
    )

def main():
    updater = Updater(TELEGRAM_API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    updater.start_polling()
    updater.idle()

# راه‌اندازی اپلیکیشن Flask
app = Flask(__name__)

@app.route('/start_game', methods=['POST'])
def start_game():
    chat_id = os.getenv("CHAT_ID")  # بهتره chat_id رو از فایل .env بگیریم
    bot = requests.get(f'https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage', params={
        'chat_id': chat_id,  # استفاده از chat_id داینامیک
        'text': 'بازی شروع شد! مبارزات آغاز می‌شود.'
    })
    if bot.status_code == 200:
        return jsonify({"status": "success", "message": "Game started!"})
    else:
        return jsonify({"status": "error", "message": "Failed to start game"}), 400

if __name__ == '__main__':
    # اول راه‌اندازی ربات تلگرام
    main()
    # سپس راه‌اندازی سرور Flask
    uvicorn.run(app, host='0.0.0.0', port=5000)
