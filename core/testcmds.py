import discord
import logging
from discord.ext import commands

Client = discord.Client()
bot = commands.Bot(command_prefix = '~~')
# Defines the test cog
class TestCMDs:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, member: discord.Member, our_input: str):
        """A simple command which repeats our input.
        In rewrite Context is automatically passed to our commands as the first argument after self."""

        await self.bot.say(our_input+" "+member.mention)
def setup(bot):
    bot.add_cog(TestCMDs(bot))