import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Approved emails
APPROVED_EMAILS = [
    "adnanbinfurquan7@gmail.com",
    "96farhanali@gmail.com"
]

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Yes ✅", callback_data="yes"),
        InlineKeyboardButton("No ❌", callback_data="no")
    )

    bot.send_message(
        message.chat.id,
        "Welcome to ForexFLY Syndicate 🚀\n\n"
        "Have you opened your trading account?",
        reply_markup=markup
    )

# Handle button clicks
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "yes":
        bot.send_message(
            call.message.chat.id,
            "Please enter your registered email address:"
        )

    elif call.data == "no":
        bot.send_message(
            call.message.chat.id,
            "❌ You need to open an account first.\n\n"
            "👉 Register using this link:\n"
            "https://my.winprofx.org/register?promo=forexfly\n\n"
            "After opening & activating your account, come back and press /start"
        )

# Handle email input
@bot.message_handler(func=lambda message: True)
def check_email(message):
    user_email = message.text.strip().lower()

    if user_email in APPROVED_EMAILS:

        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                "🔒 Click Here to Join Private Channel",
                url="https://t.me/+o6jbl-th1I1jOWM1"
            )
        )

        bot.send_message(
            message.chat.id,
            "✅ Account Verified Successfully!\n\n"
            "Click the button below to request access to the private channel:",
            reply_markup=markup
        )

    else:
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
