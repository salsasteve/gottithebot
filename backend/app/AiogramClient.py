import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from OpenAIClient import OpenAIClient

# import pyqrcode
openai = OpenAIClient()
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Hello! Im GottiTheBot")


@dp.message_handler(commands=["logo"])
async def logo(message: types.Message):
    await message.answer_photo(
        "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.coogfans.com%2Ft%2Frandom-picture-thread%2F13972&psig=AOvVaw3gTu1nQAhO03ZPgDuSGvDt&ust=1673417300065000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCPi006-rvPwCFQAAAAAdAAAAABAE"
    )


@dp.message_handler(commands=["echo"])
async def echo(message: types.Message):
    """Echo the user message."""
    if message.text == "/echo":
        await message.reply("Please type something after /echo")
    else:
        await message.reply(message.text.replace("/echo ", ""))


@dp.message_handler(commands=["ask"])
async def ask(message: types.Message):
    """Echo the user message."""
    if message.text == "/ask":
        await message.reply("Please type something after /ask")
    else:
        prompt = message.text.replace("/ask ", "")
        answer = openai.ask_question(prompt)
        await message.reply(answer)


@dp.message_handler(commands=["generate_img"])
async def generate_img(message: types.Message):
    """Echo the user message."""
    if message.text == "/generate_img":
        await message.reply("Please type something after /generate_img")
    else:
        prompt = message.text.replace("/generate_img ", "")
        image_path = openai.generate_image(prompt)
        await bot.send_photo(message.chat.id, photo=open(image_path, "rb"), caption=prompt)


# @dp.message_handler()
# async def qr(message: types.Message):
#     text = pyqrcode.create(message.text)
#     text.png('code.png', scale=5)
#     await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


async def start_polling():
    try:
        await dp.start_polling()
    finally:
        await bot.close()


# if __name__ == "__main__":
#     executor.start_polling(dp)
