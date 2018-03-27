
import discord                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import logging
import traceback
from tokenkey import *				            #Importing the secret token from token.py

enlistedroles = {'Rank 7 [Leader]', 'Rank 6 [General]', 'Rank 5 [Colonel]', 'Rank 4 [Major]', 'Rank 3 [Sergeant]', 'Rank 2 [Specialist]', 'Rank 1 [Private]'}
moderatorroles = {'Rank 7 [Leader]', 'Rank 6 [General]', 'Rank 5 [Colonel]', 'Rank 4 [Major]'}
administratorroles = {'Rank 7 [Leader]', 'Rank 6 [General]'}  
                                                # Permission System
#`u'\u274C'+' There was a error!'` 
#Current error message


version="v0.3.2"                                #Version
						
Client = discord.Client()                       # Defining The Bot
client = commands.Bot(command_prefix = "~~")
logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


@client.event                                   # On Bot startup sets game and other things
async def on_ready():
    print("SCOPED "+version+" STARTED")
    logging.info("SCOPED "+version+" STARTED")
    await client.change_presence(game=discord.Game(name="~~help", type=3))

@client.command(pass_context=True)
async def enlist(ctx, *, nickname):	         	#Bot Enlist Command
                        					    #Changes nickname
    logging.info('cmd enlist ran by: '+ctx.message.author)
    await client.change_nickname(ctx.message.author, nickname)
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Rank 1 [Private]")
    await client.add_roles(user, role)	#Adds role to user
    await client.send_message(ctx.message.author, "Thank you for enlisting in the server.\nYou are registered as `"+nickname+"`\nIf you ever with to reenlist please use `~~reenlist`!")

@client.event
async def on_member_join(member):    		# On Member Joining the server
    strmember = str(member)
    print('[ '+strmember+' ] joined server')
    fmt = 'Welcome to the ToLate Spec Ops Discord {0.mention}!\nPlease use `~~enlist yourname` to gain access to the rest of the channels.'
    await client.send_message(discord.Object(id=426870107504115713), fmt.format(member))
@client.event
async def on_member_remove(member):
    strmember = str(member)
    logging.info('[ '+strmember+' } was kicked, banned or left the server')
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")
async def inforules(ctx):			#InfoRules, for the info channel
    logging.info('cmd inforules ran by: '+ctx.message.author)
    embed=discord.Embed(title="Rules", color=0xff8000)
    embed.add_field(name='I', value='Dont be a troll: Nobody likes people who ruins games and other things, so dont be one, or we will come for you.', inline=True)
    embed.add_field(name='II', value='No NSFW shit in here, keep that stuff in your *private* folders.', inline=True)
    embed.add_field(name='III' , value="No racist shit, swearing to a certian degree is fine, but we're not cool with racisim, i will shoot you for that.", inline=True)
    embed.add_field(name='IV' , value='In Games, listen to your damn commanders, and dont spam voice chat, cause it actually helps! ', inline=True)
    embed.add_field(name='V' , value='Generally, just use common sense, if a rank 5+ can properly say "yeah, that guy is being a ass" then yes, we will remove you.', inline=True)
    embed.set_footer(text="Generally, just dont be a dick, have fun and be nice enough that people want to stay.")
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")
async def test(ctx): 				#Nukelar's testing command
    logging.info('cmd test ran by: '+ctx.message.author)
    await client.say("Test "+ctx.message.author.mention)
@client.command(pass_context=True)
async def rules(ctx):				#Tells user to go to #info for rules
    logging.info('cmd rules ran by: '+ctx.message.author)
    await client.say(ctx.message.author.mention+" go to <#425701792790216714> for info about the rules!")
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")		#Header for the info page
async def infoheader(ctx):
    logging.info('cmd infoheader ran by: '+ctx.message.author)
    embed=discord.Embed(title="To-Late Special Operations Discord server", description="Here you can find most info about the discord server ", color=0xff8000)
    embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar/ScopedBot", icon_url="https://i.imgur.com/xBxfC7Y.png")
    embed.set_thumbnail(url="https://i.imgur.com/Tp4p4R6.png")
    embed.set_footer(text="Check out the Blocks below for different segments!")
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")		#Role info for the info page
async def inforoles(ctx):
    logging.info('cmd inforoles ran by: '+ctx.message.author)
    embed=discord.Embed(title="Roles ", description="Here is a complete reference for all the roles in the server", color=0xff8000)
    embed.add_field(name="Executive Officers", value="<@&425699779931275274> | Unit leader, final say in anything.\n<@&425699841587281932> | Generals, Only the Leader can overpower theese guys.\n ", inline=True)
    embed.add_field(name="Officers", value="<@&425700147960217600> | Colonel, Top ranked officer below general.\n<@&425700298082877440> | Major, theese players know their stuff \n", inline=True)
    embed.add_field(name="Enlisted Soldiers", value="<@&425700355964272642> | Sergeant, skilled soldiers, on their way to officer status.\n<@&425700898124201984> | Specalist, theese players have been promoted due to either respect, or skill.\n<@&425700965123883025> | Enlisted, basically everyone you are in, no more. ", inline=True)
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)

@client.command(pass_context=True)
@commands.has_any_role(*enlistedroles)
async def reenlist(ctx, *, nickname):       #Bot reEnlist Command, only changes nickname
                                         	#Changes nickname
    logging.info('cmd reenlist ran by: '+ctx.message.author)
    logging.info(ctx.message.author+' re-enlisted as: '+nickname)
    await client.change_nickname(ctx.message.author, nickname)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")		#Channel info for the info channel
async def infochannels(ctx):
    logging.info('cmd infochannels ran by: '+ctx.message.author)
    embed=discord.Embed(title="Channels ", description="List of channels and what they are used for.", color=0xff8000)
    embed.add_field(name="Important Category", value="<#425701760263520256> | Contains general info on everything.\n<#425701836909969408> | News, events and more goes here.\n<#428284360962211840> | ModLog, warns, bans and kicks are logged here. ", inline=True)
    embed.add_field(name="Arma Channels Category", value="<#425694015216812064> | General, just talk about anything arma.\n<#425702412020350996> | Put any cool screenshots (or even clips) in here! \n<#425702462952046603> | In game support and help.\n<#425702496368066581> | Find a cool server? Post it details in here.\n<#428284312526389250> | Bot Commands in here and only in here... ", inline=True)
    embed.set_footer(text="#enlist, VCs and officer channels are not included here. ")
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")		#General info for the info channel
async def infogeneral(ctx):
    logging.info('cmd infogeneral ran by: '+ctx.message.author)
    embed=discord.Embed(title="General Info ", description="", color=0xff8000)
    embed.add_field(name="Overview", value="This channel contains most of the info you will need to know about our server, please read before asking for help!", inline=True)
    embed.add_field(name="Links", value="Discord Invite | https://discord.gg/fCkP7gB\nUnit Link | https://units.arma3.com/unit/tolate\nBot Code, for those interested | https://github.com/Nuk3lar/ScopedBot ", inline=True)
    embed.set_footer(text="Read on to find out more!")
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)

@client.event
async def on_command_error(ctx, error):
     #Gets the message object
    logging.error(error) #logs the error
    await client.send_message(discord.Object(id=428284312526389250), u'\u274C'+' There was a error!')

client.run(token)				#Runs the script through the specified bot token

