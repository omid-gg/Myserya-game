from telegram.ext import Updater, CommandHandler
from telegram import InputFile

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


def send_html(update, context):
    chat_id = update.effective_chat.id
    with open("index.html", "rb") as file:
        context.bot.send_document(chat_id=chat_id, document=InputFile(file), filename="Mysterya_Game.html")

dispatcher.add_handler(CommandHandler("gethtml", send_html))
