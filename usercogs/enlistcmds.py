import discord, sys, asyncio, logging                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from usercogs.userperms import enlistedroles

Client = discord.Client()
bot = commands.Bot(command_prefix = '~~')

class enlistcmds:

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='enlist')
    async def enlist(self, ctx, *, nickname):	         	#Bot Enlist Command
                        					    #Changes nickname
        author = str(ctx.message.author)
        logging.info('cmd enlist ran by: '+author)
        await bot.change_nickname(ctx.message.author, nickname)
        user = ctx.message.author
        role = discord.utils.get(user.server.roles, name="Rank 1 [Private]")
        await bot.add_roles(user, role)	#Adds role to user
        await bot.send_message(ctx.message.author, "Thank you for enlisting in the server.\nYou are registered as `"+nickname+"`\nIf you ever with to reenlist please use `~~reenlist`!")

    @bot.command(name='reenlist', aliases=['re-enlist'])
    @commands.has_any_role(*enlistedroles)
    @commands.cooldown(1, 604800, commands.BucketType.user)
    async def reenlist(self, ctx, *, nickname):       #Bot reEnlist Command, only changes nickname
                                         	#Changes nickname
        author = str(ctx.message.author)
        logging.info('cmd reenlist ran by: '+author)
        logging.info(author+' re-enlisted as: '+nickname)
        await bot.change_nickname(ctx.message.author, nickname)
        await bot.send_message(ctx.message.channel, "You have re-enlsited as: `"+nickname+"`\nKeep in mind, you can only do this once a week!")

def setup(bot):
    bot.add_cog(enlistcmds(bot))