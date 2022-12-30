from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os
from Openai_wrapper import ask_question, generate_image



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

def unknown(update: Update, context: CallbackContext):
    """Send a message when the command is unknown."""
    update.message.reply_text("Sorry, I didn't understand that command.")

def generate_img(update: Update, context: CallbackContext):
    """Generate an image from a prompt"""
    if update.message.text == "/generate_img":
        update.message.reply_text("Please type something after /generate_img")
    else:
        prompt = update.message.text.replace("/generate_img ", "")
        image_path, caption = generate_image(prompt)
        update.message.bot.send_photo(update.message.chat_id, photo=open(image_path, "rb"), caption=caption)

def main():

    TOKEN = os.getenv("TELEGRAM_TOKEN")

    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('echo', echo))
    updater.dispatcher.add_handler(CommandHandler('ask', ask))
    updater.dispatcher.add_handler(CommandHandler('generate_img', generate_img))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()


if __name__ == '__main__':
    main()
