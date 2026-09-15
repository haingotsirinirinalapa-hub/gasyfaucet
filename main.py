import telebot
import os
from flask import Flask
import threading

BOT_TOKEN = "8727352846:AAH6CP-_1vK-8ElXPeMZJBJwM_Example_Token"
CHANNEL = "@GasyCriptoFaucet"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "GasyFaucet Bot is Live!"

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    text = f"Salama {user}! Tongasoa ao @ Gasy Faucet"
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("💰 Claim", callback_data="claim"))
    markup.add(telebot.types.InlineKeyboardButton("📢 Channel", url="https://t.me/GasyCriptoFaucet"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def claim(call):
    bot.answer_callback_query(call.id, "Nahazo 0.001$!")
    bot.send_message(call.message.chat.id, "Balance: 0.001$")

def run_bot():
    bot.infinity_polling(none_stop=True)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
