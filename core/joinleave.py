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
    async def on_member_join(self, member):    		# On Member Joining the server
        strmember = str(member)
        print('[ '+strmember+' ] joined server')
        fmt = 'Welcome to the ToLate Spec Ops Discord {0.mention}!\nPlease use `~~enlist yourname` to gain access to the rest of the channels.'
        await bot.send_message(discord.Object(id=426870107504115713), fmt.format(member))
    @bot.event
    async def on_member_remove(self, member):       # On member Leaving server
        strmember = str(member)
        logging.info('[ '+strmember+' } was kicked, banned or left the server')

# Sets the cog up
def setup(bot):
    bot.add_cog(joinleave)