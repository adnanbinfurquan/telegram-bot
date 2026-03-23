import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# TOKEN from Railway
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Approved emails (ACTIVE USERS ONLY)
APPROVED_EMAILS = [
    "adnanbinfurquan7@gmail.com",
    "96farhanali@gmail.com"
]

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Welcome to ForexFLY Private Signals Bot 🚀\n\nPlease enter your registered email:"
    )

# Handle email input
@bot.message_handler(func=lambda message: True)
def check_email(message):
    user_email = message.text.strip().lower()

    if user_email in APPROVED_EMAILS:
        # Approved user
        markup = InlineKeyboardMarkup()
        button = InlineKeyboardButton(
            "👉 Click Here to Join Channel",
            url="https://t.me/+o6jbl-th1I1jOWM1"
        )
        markup.add(button)

        bot.send_message(
            message.chat.id,
            "✅ Access Approved!\n\nWelcome to Private Gold Signals 💰\n\n"
            "You will get:\n"
            "• High Accuracy Signals\n"
            "• Live Trading Sessions\n"
            "• Full Price Action Support\n\n"
            "Click below to join 👇",
            reply_markup=markup
        )

    else:
        # Not approved
        bot.send_message(
            message.chat.id,
            "❌ Your account is not active.\n\n"
            "Please make sure:\n"
            "• Your account is registered\n"
            "• Your account is active\n"
            "• Trades should be open in your account\n\n"
            "👉 Open account using this link:\n"
            "https://my.winprofx.org/register?promo=forexfly"
        )

# Run bot
bot.infinity_polling()
