# Scoped Bot by Nuk3lar, bot for the To-Late Spec Ops discord server
# Repo link: https://github.com/Nuk3lar/ScopedBot
# Github link: https://github.com/Nuk3lar

# Imports Modules 
import discord, sys, asyncio, logging, traceback, datetime
from time import gmtime, strftime

from discord.ext.commands import Bot
from discord.ext import commands
from core.config import token, Client, bot, initial_extensions

# Defines the version
version="v0.7"
outtime = strftime("%Y-%m-%d %H:%M", gmtime())
# Formats the logging template
logging.basicConfig(filename='logs\\LOG '+outtime+' output.log', filemode='w', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


                      
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(extension+" loaded!")
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc() 

# Process for when the bot starts correctly
@bot.event
async def on_ready():
    print("\n\nSCOPED "+version+" STARTED")
    logging.info("SCOPED "+version+" STARTED")
    await bot.change_presence(activity=discord.Activity(name='~~help', type=3, afk=True))


# Runs the bot in the defined token
bot.run(token, bot=True, reconnect=True)