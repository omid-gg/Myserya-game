from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from uuid import uuid4

# توکن ربات
TOKEN = "7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc"

# لینک فایل HTML
WEB_APP_URL = "https://omid-gg.github.io/Mysterya-game/index.html"  # لینک فایل HTML

# دستور /start
def start(update, context):
    chat_id = update.effective_chat.id

    # ساخت دکمه Web App
    keyboard = [[InlineKeyboardButton("Open Game", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=chat_id,
        text="Welcome to Mysterya Game! Click the button below to start:",
        reply_markup=reply_markup
    )

# هندل کردن inline query
def inline_query(update, context):
    query = update.inline_query.query

    # تعریف Web App به عنوان پاسخ
    result = InlineQueryResultArticle(
        id=uuid4(),
        title="Open Game",
        input_message_content=InputTextMessageContent("Click the button below to open the game."),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Game", web_app={"url": WEB_APP_URL})]])
    )

    # ارسال پاسخ
    update.inline_query.answer([result])

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # اضافه کردن دستور /start
    dispatcher.add_handler(CommandHandler("start", start))

    # اضافه کردن هندلر برای inline query
    dispatcher.add_handler(InlineQueryHandler(inline_query))


    # اجرای ربات
    updater.start_polling()
    updater.idle()
