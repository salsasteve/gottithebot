import os

import discord
from discord.ext import commands


class DiscordClient(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            intents=discord.Intents.all(),
            help_command=commands.DefaultHelpCommand(dm_help=True),
        )

    async def setup_hook(self):
        print(f"Logged in as {self.user.name}")
        for folder in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder, "cog.py")):
                await self.load_extension(f"modules.{folder}.cog")
        print("Loaded cogs")
