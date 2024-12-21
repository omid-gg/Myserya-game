import os
import logging
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask, request
import requests

load_dotenv()

# دریافت توکن از فایل .env
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

app = Flask(__name__)

# تنظیمات لاگینگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور استارت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"سلام {update.effective_user.first_name}! خوش اومدی. آماده بازی هستی؟")

    bot = Bot(TELEGRAM_API_TOKEN)
    dispatcher = bot.dispatcher
    set_up_dispatcher(dispatcher)
    set_webhook()  # تنظیم Webhook
    app.run(host='0.0.0.0', port=5000, debug=True)  # اجرای سرور Flask
