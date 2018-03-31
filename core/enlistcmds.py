import discord, sys, asyncio, logging                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.perms import enlistedroles, unenlistedroles

Client = discord.Client()
bot = commands.Bot(command_prefix = '~~')

class enlistcmds:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*unenlistedroles)
    async def enlist(self, message, *, nickname: str):	         	#Bot Enlist Command
                        					    #Changes nickname
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('CMD ~~enlist ran by user ID: '+memberid)
        await member.edit(nick=nickname)
        user = member
        roleadd = discord.utils.get(user.guild.roles, id=425700965123883025)
        await member.add_roles(roleadd)	#Adds role to user
        roleremove = discord.utils.get(user.guild.roles, id=429694539851366421)
        await member.remove_roles(roleremove)
        await member.create_dm()      #Makes a DM with user
        channel = member.dm_channel         #Sets channel var
        embed=discord.Embed(title='Thanks for enlisting!', description='You have enlisted as `'+nickname+'`!', color=0xff8000)
        embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
        embed.add_field(name='You can use command reenlist to change your nickname.', value='Example: `~~reenlist yourname`', inline=True)
        await channel.send(embed=embed)
        logging.info('User ID: '+memberid+' enlisted as: '+nickname)

    @commands.command()
    @commands.has_any_role(*enlistedroles)
    async def reenlist(self, message, *, nickname: str):       #Bot reEnlist Command, only changes nickname
                                         	#Changes nickname
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('CMD ~~enlist ran by user ID: '+memberid)
        await member.edit(nick=nickname)
        await member.create_dm()      #Makes a DM with user
        channel = member.dm_channel         #Sets channel var
        embed=discord.Embed(title='You reenlisted', description='You have reenlisted as `'+nickname+'`!', color=0xff8000)
        embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
        embed.add_field(name='You can use command reenlist to change your nickname.', value='Example: `~~reenlist yourname`', inline=True)
        await channel.send(embed=embed)
        logging.info('User ID: '+memberid+' reenlisted as: '+nickname)

def setup(bot):
    bot.add_cog(enlistcmds(bot))