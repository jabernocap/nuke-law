import os, sys, discord, requests, json, threading, random, asyncio, logging
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime

client = commands.Bot(command_prefix = '.')

os.system("title law")

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

with open("Law/Settings.json") as f:
	settings = json.load(f)
token = settings.get("Token")
prefix = settings.get("Prefix")
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
Webhook_users = settings.get("Webhook Usernames")
Webhook_contents = settings.get("Spam Messages")
bot = settings.get("Bot")

if bot:
	headers = {
	  "Authorization": f"Bot {token}"
	}
else:
	headers = {
	  "Authorization": token
	}

law = commands.Bot(
  command_prefix=prefix,
  intents=discord.Intents.all(),
  help_command=None
)

sessions = requests.Session()
clear()

law.logo = ('''
\033[38;5;85m                                                              ╦   ╔═╗ ╦ ╦
\033[38;5;84m                                                              ║   ╠═╣ ║║║
\033[38;5;83m                                                              ║   ║ ║ ║║║
\033[38;5;82m                                                              ╩═╝ ╩ ╩ ╚╩╝
\033[38;5;81m                                                            ─┼─┼─┼─┼─┼─┼─┼─
''')

clear()
print(law.logo)

help_command=None

@law.event
async def on_ready():
  print('Have Fun!')

@law.command(name='help')
async def help(ctx):
  await ctx.send('help - This command shows this message')

client.run('')