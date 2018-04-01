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
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('User ID [ '+memberid+' ] Joined the server')
        channel = self.bot.get_channel(426870107504115713)
        user = member
        role = discord.utils.get(user.guild.roles, id=429694539851366421)
        await member.add_roles(role)
        await channel.send('Welcome to the ToLate Spec Ops Discord '+member.mention+'!\nPlease use `~~enlist yourname` to gain access to the rest of the channels.')
    @bot.event
    async def on_member_remove(self, member: discord.Member):       # On member Leaving server
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('User ID [ '+memberid+' ] was kicked, banned or left the server')

# Sets the cog up
def setup(bot):
    bot.add_cog(joinleave(bot))