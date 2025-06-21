import os
import django
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from decouple import config

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from telegrambot.models import TelegramUser


def start(update: Update, context: CallbackContext):
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    if not username:
        username = f"user_{chat_id}"  # fallback identifier

    obj, created = TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={'username': username}
    )

    if created:
        update.message.reply_text(f"Hi {username}, you're now registered!")
        print(f"New user registered: {username}")
    else:
        update.message.reply_text(f"Hi {username}, you're already registered.")
        print(f"User already exists: {username}")



def main():
    token = config('TELEGRAM_BOT_TOKEN')
    print("Loaded token:", token)

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    print("Bot is polling... waiting for /start commands.")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
