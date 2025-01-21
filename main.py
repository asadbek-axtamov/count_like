from telegram.ext import Updater,MessageHandler
from telegram import Bot, Update
import os

def echo(update: Update, context):
    print(update.message.text)

TOKEN = os.getenv("TOKEN")

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

# add handlers here

dispatcher.add_handler(MessageHandler(filters=None,callback=echo))

updater.start_polling()
updater.idle()