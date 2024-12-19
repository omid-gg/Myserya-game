from flask import Flask, request
import telegram

# توکن ربات تلگرام
TOKEN = "7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc"
bot = telegram.Bot(token=TOKEN)

# اپلیکیشن Flask
app = Flask(__name__)

# مسیر وب‌هوک
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        if "text" in data["message"]:
            text = data["message"]["text"]

            if text == "/start":
                bot.send_message(
                    chat_id=chat_id,
                    text="Welcome to Mysterya! Click below to start the game.",
                    reply_markup=telegram.InlineKeyboardMarkup(
                        [[telegram.InlineKeyboardButton("Play Game", web_app={"url": "https://mysterya-game.vercel.app"})]]
                    ),
                )

    return "OK"

# نقطه ورود اپلیکیشن
if __name__ == "__main__":
    app.run(port=5000)
