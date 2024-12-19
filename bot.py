from telegram.ext import Updater, CommandHandler

# دستور /start
def start(update, context):
    update.message.reply_text("سلام! به Mystery Land خوش اومدی. آماده ماجراجویی هستی؟")

# دستور /help
def help_command(update, context):
    update.message.reply_text("دستورات: \n/start - شروع بازی \n/help - راهنما")

# توکن رباتت رو اینجا بذار
TOKEN = "7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc"

# تنظیم ربات
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# اضافه کردن دستورات
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

# اجرای ربات
updater.start_polling()
updater.idle()
