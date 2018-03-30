# Scoped Bot by Nuk3lar, bot for the To-Late Spec Ops discord server
# Repo link: https://github.com/Nuk3lar/ScopedBot
# Github link: https://github.com/Nuk3lar

# Imports Modules 
import discord, sys, asyncio, logging, traceback     
from discord.ext.commands import Bot
from discord.ext import commands
from core.tokenkey import token

# Defines the version
version="v0.3.6"

# Formats the logging template
logging.basicConfig(filename='output.log', filemode='w', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Defines the client and bot prefix
Client = discord.Client()
bot = commands.Bot(command_prefix = "~~")

# Defines extentions (files) and loads them into the bot
initial_extensions = ['usercogs.enlistcmds',
                      'core.joinleave']
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(extension+" loaded!")
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc() 

# Process for when the bot starts correctly
async def on_ready():
    print("SCOPED "+version+" STARTED")
    logging.info("SCOPED "+version+" STARTED")
    await bot.change_presence(game=discord.Game(name="~~help", type=3))

# Runs the bot in the defined token
bot.run(token, bot=True, reconnect=True)