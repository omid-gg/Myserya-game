from telegram.ext import Updater, CommandHandler

TOKEN = "7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc"

def start(update, context):
    update.message.reply_text("سلام! ربات تلگرام آماده است.")

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)

    # اضافه کردن دستور /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # شروع ربات
    updater.start_polling()
    updater.idle()
