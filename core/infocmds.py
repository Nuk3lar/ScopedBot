# Imports all the modules
import discord, sys, asyncio, logging, traceback     
from discord.ext.commands import Bot
from discord.ext import commands
from core.perms import administratorroles

Client = discord.Client()

class InfoCMDs:
    def __init__(self, bot):
        self.bot = bot
    # INFO CHANNEL TEMPLATE
    # infoheader
    # infogeneral
    # inforules
    # infochannels
    # inforoles
    
    @commands.command()
    @commands.has_any_role(*administratorroles)
    @commands.guild_only()
    async def infoadm(self, message, *, part: str):
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('CMD ~~infoadm ran by User ID: '+memberid)
        channel = self.bot.get_channel(425701760263520256)
        if part == 'header':
            embed=discord.Embed(title="To-Late Special Operations Discord server", description="Here you can find most info about the discord server ", color=0xff8000)
            embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar/ScopedBot", icon_url="https://i.imgur.com/xBxfC7Y.png")
            embed.set_thumbnail(url="https://i.imgur.com/Tp4p4R6.png")
            embed.set_footer(text="Check out the Blocks below for different segments!")
            await channel.send('', embed=embed)
        if part == 'general':
            embed=discord.Embed(title="General Info ", description="", color=0xff8000)
            embed.add_field(name="Overview", value="This channel contains most of the info you will need to know about our server, please read before asking for help!", inline=True)
            embed.add_field(name="Links", value="Discord Invite | https://discord.gg/fCkP7gB\nUnit Link | https://units.arma3.com/unit/tolate\nBot Code, for those interested | https://github.com/Nuk3lar/ScopedBot ", inline=True)
            embed.set_footer(text="Read on to find out more!")
            await channel.send('', embed=embed)
        if part == 'rules':
            embed=discord.Embed(title="Rules", color=0xff8000)
            embed.add_field(name='I', value='Dont be a troll: Nobody likes people who ruins games and other things, so dont be one, or we will come for you.', inline=True)
            embed.add_field(name='II', value='No NSFW shit in here, keep that stuff in your *private* folders.', inline=True)
            embed.add_field(name='III' , value="No racist shit, swearing to a certian degree is fine, but we're not cool with racisim, i will shoot you for that.", inline=True)
            embed.add_field(name='IV' , value='In Games, listen to your damn commanders, and dont spam voice chat, cause it actually helps! ', inline=True)
            embed.add_field(name='V' , value='Generally, just use common sense, if a rank 5+ can properly say "yeah, that guy is being a ass" then yes, we will remove you.', inline=True)
            embed.set_footer(text="Generally, just dont be a dick, have fun and be nice enough that people want to stay.")
            await channel.send('', embed=embed)
        if part == 'channels':
            embed=discord.Embed(title="Channels ", description="List of channels and what they are used for.", color=0xff8000)
            embed.add_field(name="Important Category", value="<#425701760263520256> | Contains general info on everything.\n<#425701836909969408> | News, events and more goes here.\n<#428284360962211840> | ModLog, warns, bans and kicks are logged here. ", inline=True)
            embed.add_field(name="Arma Channels Category", value="<#425694015216812064> | General, just talk about anything arma.\n<#425702412020350996> | Put any cool screenshots (or even clips) in here! \n<#425702462952046603> | In game support and help.\n<#425702496368066581> | Find a cool server? Post it details in here.\n<#428284312526389250> | Bot Commands in here and only in here... ", inline=True)
            embed.set_footer(text="#enlist, VCs and officer channels are not included here. ")
            await channel.send('', embed=embed)
        if part == 'roles':
            embed=discord.Embed(title="Roles ", description="Here is a complete reference for all the roles in the server", color=0xff8000)
            embed.add_field(name="Executive Officers", value="<@&425699779931275274> | Unit leader, final say in anything.\n<@&425699841587281932> | Generals, Only the Leader can overpower theese guys.\n ", inline=True)
            embed.add_field(name="Officers", value="<@&425700147960217600> | Colonel, Top ranked officer below general.\n<@&425700298082877440> | Major, theese players know their stuff \n", inline=True)
            embed.add_field(name="Enlisted Soldiers", value="<@&425700355964272642> | Sergeant, skilled soldiers, on their way to officer status.\n<@&425700898124201984> | Specalist, theese players have been promoted due to either respect, or skill.\n<@&425700965123883025> | Enlisted, most people in the server.", inline=True)
            embed.add_field(name="Unenlisted People", value="<@&429694539851366421> | Un-Enlisted people, they haven't even enlisted yet.", inline=True)
            await channel.send('', embed=embed)
def setup(bot):
    bot.add_cog(InfoCMDs(bot))