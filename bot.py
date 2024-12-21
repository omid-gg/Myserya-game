from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
from dotenv import load_dotenv
import os

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# خواندن توکن ربات از فایل .env
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

if not TELEGRAM_API_TOKEN:
    raise ValueError("توکن ربات تلگرام در فایل .env تعریف نشده است.")

# تنظیمات لاگ‌ها
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

def main():
    updater = Updater(TELEGRAM_API_TOKEN)
    dispatcher = updater.dispatcher

    # ثبت دستورات
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    # اجرای ربات
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
