"""import os

from dotenv import load_dotenv

from discord.ext import  commands
from click import command

import urllib.request
import json

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot =commands.Bot(command_prefix="-")
@bot.comaand(name="suma")
async def sumar(ctx,num1,num2):
    reponse =num1+num2
    await ctx.send(reponse)

bot.run(TOKEN)"""
