import asyncio
import os

from AiogramClient import start_polling
from DiscordClient import DiscordClient
from dotenv import load_dotenv


async def discord_poll(token: str):
    client = DiscordClient()
    await client.start(token)


async def main():
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    await asyncio.gather(discord_poll(DISCORD_TOKEN), start_polling())


if __name__ == "__main__":
    asyncio.run(main())
