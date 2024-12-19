from telegram.ext import ApplicationBuilder, CommandHandler, InlineQueryHandler, CallbackContext
from uuid import uuid4

# شروع بوت
TOKEN = "7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc"

# لینک وب اپ
WEB_APP_URL = "https://mysterya-game.vercel.app"

# دستور /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Game", web_app={"url": WEB_APP_URL})],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below to open the game:", reply_markup=reply_markup)

# هندل کردن inline query
async def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query

    result = InlineQueryResultArticle(
        id=str(uuid4()),
        title="Open Game",
        input_message_content=InputTextMessageContent("Click the button below to open the game."),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Game", web_app={"url": WEB_APP_URL})]])
    )

    await update.inline_query.answer([result])

# ساخت برنامه
app = ApplicationBuilder().token(TOKEN).build()

# اضافه کردن هندلرها
app.add_handler(CommandHandler("start", start))
app.add_handler(InlineQueryHandler(inline_query))

# شروع برنامه با Polling
app.run_polling()