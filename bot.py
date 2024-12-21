import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask, request
import requests

load_dotenv()

# دریافت توکن از فایل .env
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

app = Flask(__name__)

# تنظیمات لاگینگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور استارت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f"سلام {update.effective_user.first_name}! خوش اومدی. آماده بازی هستی؟"
    )

# دستور بازی
def play(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("بازی شروع شد! موفق باشی.")

# ثبت دستورات ربات
def set_up_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

# ایجاد Webhook برای دریافت پیام‌ها
@app.route(f'/{TELEGRAM_API_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, bot)
    dispatcher.process_update(update)
    return 'ok'

# راه‌اندازی Webhook در تلگرام
def set_webhook():
    url = f"https://yourdomain.com/{TELEGRAM_API_TOKEN}"  # باید دامنه و مسیر خود را قرار دهید
    set_url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/setWebhook?url={url}"
    response = requests.get(set_url)
    if response.status_code == 200:
        logger.info("Webhook set successfully!")
    else:
        logger.error(f"Failed to set webhook: {response.status_code}")

# راه‌اندازی اپلیکیشن Flask
if __name__ == '__main__':
    # تنظیمات Webhook
    bot = Updater(TELEGRAM_API_TOKEN).bot
    dispatcher = bot.dispatcher
    set_up_dispatcher(dispatcher)
    set_webhook()  # تنظیم Webhook
    app.run(host='0.0.0.0', port=5000, debug=True)  # اجرای سرور Flask
