# Imports all the modules
import discord, sys, asyncio, logging, traceback     
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot = commands.Bot(command_prefix = '~~')

# Join leave cog
class joinleave:
    
    def __init__(self, bot):
        self.bot = bot

    
    @bot.event
    async def on_member_join(self, member: discord.Member):    		# On Member Joining the server
        strmember = str(member)
        logging.info('[ '+strmember+' ] Joined the server')
        channel = self.bot.get_channel(426870107504115713)
        await channel.send('Welcome to the ToLate Spec Ops Discord '+member.mention+'!\nPlease use `~~enlist yourname` to gain access to the rest of the channels.')
    @bot.event
    async def on_member_remove(self, member: discord.Member):       # On member Leaving server
        strmember = str(member)
        logging.info('[ '+strmember+' ] was kicked, banned or left the server')

# Sets the cog up
def setup(bot):
    bot.add_cog(joinleave(bot))