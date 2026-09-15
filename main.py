import telebot
import time

BOT_TOKEN = "8727352846:AAH6CP-_1vK-8ElXPeMZJBeAmiSRBNTLVgo"
CHANNEL = "@GasyCriptoFaucet"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    text = f"Salama {user}! Tongasoa ao @ GasyFaucet MG!\n\nMahazoa 100 Satoshi isan'ora!"
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("CLAIM 100 SAT", callback_data="claim"))
    markup.add(telebot.types.InlineKeyboardButton("CANAL", url="https://t.me/GasyCriptoFaucet"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "claim")
def claim(call):
    bot.answer_callback_query(call.id, "Nahazo 100 Satoshi ianao!")
    bot.send_message(call.message.chat.id, "Balance-nao: 100 SAT\nAfaka 1 ora vao afaka mi-claim indray.")

bot.infinity_polling()
