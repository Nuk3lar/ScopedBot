import discord                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

enlistedroles = {'Rank 7 [Leader]', 'Rank 6 [General]', 'Rank 5 [Colonel]', 'Rank 4 [Major]', 'Rank 3 [Sergeant]', 'Rank 2 [Specialist]', 'Rank 1 [Private]'}

version="v0.3"
						#Defines secret bot token
with open ("token.txt", "r") as tokenfile:
    token=tokenfile.readlines()
Client = discord.Client()                       # Defining The Bot
client = commands.Bot(command_prefix = "~~")
@client.event                                   # On Bot startup sets game and other things
async def on_ready():
    print("SCOPED "+version+" STARTED")
    await client.change_presence(game=discord.Game(name="~~help", type=3))
@client.command(pass_context=True)
async def enlist(ctx, *, nickname):		#Bot Enlist Command
    try:					#Changes nickname
        print("USER ENLISTED as "+nickname)
        await client.change_nickname(ctx.message.author, nickname)
        user = ctx.message.author
        role = discord.utils.get(user.server.roles, name="Rank 1 [Private]")
        await client.add_roles(user, role)	#Adds role to user
        await client.send_message(discord.Object

    
    except:
        await client.send_message(discord.Object(id=426870107504115713),u'\u274C'+' There was a error!')
@client.event
async def on_member_join(member):    		# On Member Joining the server
    print('Member joined server')
    embed=discord.Embed(title='Welcome to the ToLate Arma3 server!' , description=' To get started, enlist with your Arma3 ign with `~~enlist yourname`', color=0xff8040)
    embed.set_author(name='Scoped Bot', url='https://github.com/Nuk3lar',icon_url='https://i.imgur.com/xBxfC7Y.png')
    embed.set_thumbnail(url='https://i.imgur.com/Tp4p4R6.png')
    await client.send_message(discord.Object(id=426870107504115713),embed=embed)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")
async def inforules(ctx):			#InfoRules, for the info channel
    print('CMD inforules WAS RAN')
    embed=discord.Embed(title="Rules", color=0xff8000)
    embed.add_field(name='I', value='Dont be a troll: Nobody likes people who ruins games and other things, so dont be one, or we will come for you.', inline=True)
    embed.add_field(name='II', value='No NSFW shit in here, keep that stuff in your *private* folders.', inline=True)
    embed.add_field(name='III' , value='No racist shit, swearing to a certian degree is fine, but were not cool with racisim, i will shoot you for that.', inline=True)
    embed.add_field(name='IV' , value='In Games, listen to your damn commanders, and dont spam voice chat, cause it actually helps! ', inline=True)
    embed.add_field(name='V' , value='Generally, just use common sense, if a rank 5+ can properly say "yeah, that guy is being a ass" then yes, we will remove you.', inline=True)
    embed.set_footer(text="Generally, just dont be a dick, have fun and be nice enough that people want to stay.")
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")
async def test(ctx): 				#Nukelar's testing command
    print('CMD test WAS RAN')
    await client.say("Test "+ctx.message.author.mention)
@client.command(pass_context=True)
async def rules(ctx):				#Tells user to go to #info for rules
    print('CMD rules WAS RAN')
    await client.say(ctx.message.author.mention+" go to <#425701792790216714> for info about the rules!")
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")		#Header for the info page
async def infoheader(ctx):
    print('CMD infoheader WAS RAN')
    embed=discord.Embed(title="To-Late Special Operations Discord server", description="Here you can find most info about the discord server ", color=0xff8000)
    embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar", icon_url="https://i.imgur.com/xBxfC7Y.png")
    embed.set_thumbnail(url="https://i.imgur.com/Tp4p4R6.png")
    embed.set_footer(text="Check out the Blocks below for different segments!")
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)
@client.command(pass_context=True)
@commands.has_role("Rank 7 [Leader]")		#Role info for the info page
async def inforoles(ctx):
    print('CMD inforoles WAS RAN')
    embed=discord.Embed(title="Roles ", description="Here is a complete reference for all the roles in the server", color=0xff8000)
    embed.add_field(name="Executive Officers", value="<@&425699779931275274> | Unit leader, final say in anything.\n<@&425699841587281932> | Generals, Only the Leader can overpower theese guys.\n ", inline=True)
    embed.add_field(name="Officers", value="<@&425700147960217600> | Colonel, Top ranked officer below general.\n<@&425700298082877440> | Major, theese players know their stuff \n", inline=True)
    embed.add_field(name="Enlisted Soldiers", value="<@&425700355964272642> | Sergeant, skilled soldiers, on their way to officer status.\n<@&425700898124201984> | Specalist, theese players have been promoted due to either respect, or skill.\n<@&425700965123883025> | Enlisted, basically everyone you are in, no more. ", inline=True)
    await client.send_message(discord.Object(id=425701760263520256),embed=embed)

@client.command(pass_context=True)
@commands.has_any_role(*enlistedroles)
async def reenlist(ctx, *, nickname):           #Bot reEnlist Command, only changes nickname
                                         	#Changes nickname
    print("USER re_ENLISTED as "+nickname)
    await client.change_nickname(ctx.message.author, nickname)
client.run(token)				#Runs the script through the specified bot token
