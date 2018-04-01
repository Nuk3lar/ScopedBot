import discord, sys, asyncio, logging                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import Client, bot, unenlistedroles, enlistedroles


class enlistcmds:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*unenlistedroles)
    @commands.guild_only()
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
        embed.add_field(name='You can use command reenlist to change your nickname.', value='Example: `~~reenlist (yourname)`', inline=True)
        await channel.send(embed=embed)
        logging.info('User ID: '+memberid+' enlisted as: '+nickname)

    @commands.command()
    @commands.has_any_role(*enlistedroles)
    @commands.guild_only()
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
        embed.add_field(name='You can use command reenlist to change your nickname.', value='Example: `~~reenlist (yourname)`', inline=True)
        await channel.send(embed=embed)
        logging.info('User ID: '+memberid+' reenlisted as: '+nickname)
class HelpCMD:
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_any_role(*enlistedroles)
    async def help(self, message, *, part=None):
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('CMD ~~help ran by user ID: '+memberid)
        if part is None:
            embed=discord.Embed(title="Help for Scoped Bot", description="List of commands\n(part) | Required variable\n[part] | Optional variable\nDont include the brackets used in examples!", color=0xff8000)
            embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar/ScopedBot", icon_url="https://i.imgur.com/xBxfC7Y.png")
            embed.set_thumbnail(url="https://i.imgur.com/Tp4p4R6.png")
            embed.add_field(name='Commands', value='`~~enlist` | Only usable by <@&429694539851366421> because it is the verification command.\n`~~reenlist` | Use to change your nickname.\n`~~help` | Shows help menu, or help on specified command.\n`~~rules` | Directs you to <#425701760263520256>\n`~~modhelp` | Help for Rank 4 users and above' , inline=False)
            embed.set_footer(text="Use ~~help [cmd] to view specific help and usage info on a command!")
            channel = message.channel
            await channel.send('', embed=embed)
        if part == 'enlist':
            embed=discord.Embed(title='Help for command: '+part, color=0xff8000)
            embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
            embed.add_field(name='Usage', value='~~'+part+' (yourname)', inline=False)
            embed.add_field(name='Inputs (Required)', value='yourname | this determines the name you will be assigned after enlisting', inline=True)
            embed.add_field(name='Note:', value='This command can only be used by users with <@&429694539851366421>, if you want to reenlist use ~~reenlist.', inline=True)
            channel = message.channel
            await channel.send('', embed=embed)
        if part == 'reenlist':
            embed=discord.Embed(title='Help for command: '+part, color=0xff8000)
            embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
            embed.add_field(name='Usage', value='~~'+part+' (yourname)', inline=False)
            embed.add_field(name='Inputs (Required)', value='yourname | what your name will be changed to.', inline=True)
            channel = message.channel
            await channel.send('', embed=embed)
        if part == 'help':
            embed=discord.Embed(title='Help for command: '+part, color=0xff8000)
            embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
            embed.add_field(name='Usage', value='~~'+part+' (yourname)', inline=False)
            embed.add_field(name='Inputs [Optional]', value='(cmd) | if you include a name of a command, it will show info for it!', inline=True)
            channel = message.channel
            await channel.send('', embed=embed)
        if part == 'rules':
            embed=discord.Embed(title='Help for command: '+part, color=0xff8000)
            embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
            embed.add_field(name='Usage', value='~~'+part+' (yourname)', inline=False)
            embed.add_field(name='No inputs for this command', value='', inline=True)
            channel = message.channel
            await channel.send('', embed=embed)

        
def setup(bot):
    bot.add_cog(enlistcmds(bot))
    bot.remove_command("help")
    bot.add_cog(HelpCMD(bot))
    
    