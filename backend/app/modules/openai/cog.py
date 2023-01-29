from discord import File
from discord.ext import commands
from OpenAIClient import OpenAIClient


class OpenAICog(commands.Cog, name="OpenAI Commands"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.openai = OpenAIClient()

    @commands.command()
    async def ask(self, ctx: commands.Context, *, question: str):
        """Response to a question from openai

        :param ctx: default context
        :type ctx: commands.Context
        :param question: question to ask openai
        :type question: List[str]
        """

        answer = self.openai.ask_question(question)
        await ctx.send(answer)

    @commands.command()
    async def generate_img(self, ctx: commands.Context, *, prompt: str):
        """Generate an image from a prompt

        :param ctx: default context
        :type ctx: commands.Context
        :param prompt: prompt to generate image from
        :type prompt: List[str]
        """

        image_path = self.openai.generate_image(prompt)
        await ctx.send(file=File(image_path))


async def setup(bot: commands.Bot):
    await bot.add_cog(OpenAICog(bot))
