from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dotenv import load_dotenv
import os
from Openai_wrapper import ask_question

load_dotenv()

updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, I'm OpenAI bot!")

def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    if update.message.text == "/echo":
        update.message.reply_text("Please type something after /echo")
    else:
        update.message.reply_text(update.message.text.replace("/echo ", ""))

def ask(update: Update, context: CallbackContext):
    """Ask OpenAI for a response"""
    if update.message.text == "/ask":
        update.message.reply_text("Please type something after /ask")
    else:
        question = update.message.text.replace("/ask ", "")
        answer = ask_question(question)
        update.message.reply_text(answer)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('echo', echo))
updater.dispatcher.add_handler(CommandHandler('ask', ask))

updater.start_polling()