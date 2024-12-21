import os
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Bot

# تنظیمات
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=TELEGRAM_API_TOKEN)
updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# تنظیمات لاگینگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور استارت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"سلام {update.effective_user.first_name}! خوش اومدی. آماده بازی هستی؟")

# دستور بازی
def play(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("بازی شروع شد! موفق باشی.")

# ثبت دستورات ربات
def set_up_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

# تنظیم Webhook ربات تلگرام
def set_webhook():
    url = f"https://your-vercel-app-url.vercel.app/{TELEGRAM_API_TOKEN}"  # آدرس Webhook
    webhook_url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/setWebhook?url={url}"
    response = requests.get(webhook_url)
    if response.status_code == 200:
        logger.info("Webhook set successfully!")
    else:
        logger.error(f"Failed to set webhook: {response.status_code}")

# فانکشن سرورلس برای Vercel
def handler(request):
    if request.method == "POST":
        json_str = request.get_data(as_text=True)
        update = Update.de_json(json_str, bot)
        dispatcher.process_update(update)
        return "ok"
    return "Method not allowed", 405

# اجرای Webhook
if __name__ == "__main__":
    set_webhook()  # تنظیم Webhook ربات

