
from telegram.ext import CommandHandler, Updater, MessageHandler
from telegram import Update
import os

TOKEN = os.environ['TOKEN']
votes={
    "👍":0,
    "👎":0}
def like(update, context):
    
    if update.message.text=="👍" :
        votes['👍']+=1
    elif update.message.text=="👎"  :
        votes['👎']+=1
    update.message.reply_text(f"Like : {votes['👍']} Dislike : {votes['👎']}")

    

updater=Updater(TOKEN)
dispatcher=updater.dispatcher
dispatcher.add_handler(MessageHandler(filters=None, callback=like))
updater.start_polling()
updater.idle()