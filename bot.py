from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ApplicationBuilder

# توکن ربات
TOKEN = "توکن_ربات_تو"

# لینک فایل HTML (فایل باید روی هاست یا سرور آپلود شده باشه)
WEB_APP_URL = "https://yourusername.github.io/your-repo-name/index.html"  # لینک فایل HTML

# دستور /start
async def start(update: Update, context):
    chat_id = update.effective_chat.id

    # ساخت دکمه Web App
    keyboard = [[InlineKeyboardButton("Open Game", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text="Welcome to Mysterya Game! Click the button below to start:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    # ساخت اپلیکیشن ربات
    application = ApplicationBuilder().token(TOKEN).build()

    # اضافه کردن دستور /start
    application.add_handler(CommandHandler("start", start))

    # اجرای ربات
    application.run_polling()
