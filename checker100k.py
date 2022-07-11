import discord
import json
from colorama import Fore, init
from discord.ext import commands
import os
 
client = discord.Client()
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
client.remove_command('help') 

init(convert=True)
clear = lambda: os.system('cls')




@client.event
async def on_ready():
  print(f"""
                                  
                                  {Fore.BLUE}   
NNNNNNNN        NNNNNNNN     OOOOOOOOO     RRRRRRRRRRRRRRRRR   TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH
N:::::::N       N::::::N   OO:::::::::OO   R::::::::::::::::R  T:::::::::::::::::::::TH:::::::H     H:::::::H
N::::::::N      N::::::N OO:::::::::::::OO R::::::RRRRRR:::::R T:::::::::::::::::::::TH:::::::H     H:::::::H
N:::::::::N     N::::::NO:::::::OOO:::::::ORR:::::R     R:::::RT:::::TT:::::::TT:::::THH::::::H     H::::::HH
N::::::::::N    N::::::NO::::::O   O::::::O  R::::R     R:::::RTTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H  
N:::::::::::N   N::::::NO:::::O     O:::::O  R::::R     R:::::R        T:::::T          H:::::H     H:::::H  
N:::::::N::::N  N::::::NO:::::O     O:::::O  R::::RRRRRR:::::R         T:::::T          H::::::HHHHH::::::H  
N::::::N N::::N N::::::NO:::::O     O:::::O  R:::::::::::::RR          T:::::T          H:::::::::::::::::H  
N::::::N  N::::N:::::::NO:::::O     O:::::O  R::::RRRRRR:::::R         T:::::T          H:::::::::::::::::H  
N::::::N   N:::::::::::NO:::::O     O:::::O  R::::R     R:::::R        T:::::T          H::::::HHHHH::::::H  
N::::::N    N::::::::::NO:::::O     O:::::O  R::::R     R:::::R        T:::::T          H:::::H     H:::::H  
N::::::N     N:::::::::NO::::::O   O::::::O  R::::R     R:::::R        T:::::T          H:::::H     H:::::H  
N::::::N      N::::::::NO:::::::OOO:::::::ORR:::::R     R:::::R      TT:::::::TT      HH::::::H     H::::::HH
N::::::N       N:::::::N OO:::::::::::::OO R::::::R     R:::::R      T:::::::::T      H:::::::H     H:::::::H
N::::::N        N::::::N   OO:::::::::OO   R::::::R     R:::::R      T:::::::::T      H:::::::H     H:::::::H
NNNNNNNN         NNNNNNN     OOOOOOOOO     RRRRRRRR     RRRRRRR      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH
                                       {Fore.WHITE}
{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.BLUE}North Will Afk Check For 100,001 Seconds When You Say "son";){Fore.RED}.
""")



@client.event
async def on_message(message):
    channel = message.channel
    if message.content.endswith('son'):
      for i in range(1, 100001):
        await message.channel.send(i)
    
## Gets Discord Token From The Config File

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
client.run(token, bot=False)
