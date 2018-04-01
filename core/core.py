# Imports all the modules
import discord, sys, asyncio, logging, traceback     
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import Client, bot

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


class ErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandNotFound):
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C That is not a command!', description="Please use ~~help for a list of valid commands ", color=0xb20000)
            embed.add_field(name="Make sure you input a **actual** command!", value="This includes capitalisation", inline=True)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/ScopedBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.UserInputError):
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C You did not input the command correctly!', description='Check that you have entered all the variables.' , color=0xb20000)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/ScopedBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C The bot does not have permission to do that!', description='' , color=0xb20000)
            embed.add_field(name="Please raise a issue at: ", value="https://github.com/Nuk3lar/ScopedBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.NoPrivateMessage):
            logging.error(error) #logs the error
            embed=discord.Embed(title=u"\u274C Commands can't be ran in DMs ", description='Please run commands for this bot in https://discord.gg/fCkP7gB' , color=0xb20000)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/ScopedBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.CheckFailure):
            member = ctx.message.author
            memberidint = member.id
            memberid = str(memberidint)
            logging.error('User ID: '+memberid+' tried to run command: '+ctx.command.qualified_name+' but was denied!')
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C You do not have the permissions for that!', description='If you think that is a error contact Nukelar#2781' , color=0xb20000)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/ScopedBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        else:
            logging.error(error)


# Sets the cog up
def setup(bot):
    bot.add_cog(joinleave(bot))
    bot.add_cog(ErrorHandler(bot))