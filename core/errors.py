import discord
import logging
from discord.ext import commands

Client = discord.Client()

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
        elif isinstance(error, commands.TooManyArguments):
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C Too many arguements!', description='Please check your input!' , color=0xb20000)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/ScopedBot/issues", inline=True)
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
def setup(bot):
    bot.add_cog(ErrorHandler(bot))

