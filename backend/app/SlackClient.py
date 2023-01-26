from dotenv import load_dotenv
from slack_bolt import AsyncApp

app = AsyncApp()

# @app.command("/hello")
# async def hello_command(ack, command):
#     await asyncio.sleep(5)
#     ack("Hello!")


async def start_bot():
    await app.start("SLACK_BOT_TOKEN")
