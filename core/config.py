
import discord, sys, asyncio, logging                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.tokenkey import token

Client = discord.Client()
bot = commands.Bot(command_prefix = "~~")

# Permissions
unenlistedroles = {'Un-Enlisted'}
enlistedroles = {'Rank 7 [Leader]',
                 'Rank 6 [General]',
                 'Rank 5 [Colonel]', 
                 'Rank 4 [Major]', 
                 'Rank 3 [Sergeant]', 
                 'Rank 2 [Specialist]', 
                 'Rank 1 [Private]'}
moderatorroles = {'Rank 7 [Leader]', 
                  'Rank 6 [General]', 
                  'Rank 5 [Colonel]', 
                  'Rank 4 [Major]'}	 
administratorroles = {'Rank 7 [Leader]', 
                      'Rank 6 [General]'}  

# Defines the client and bot prefix
# Defines extentions (files) and loads them into the bot
initial_extensions = ['core.core',
                      'core.usercmds',
                      'core.modcmds']