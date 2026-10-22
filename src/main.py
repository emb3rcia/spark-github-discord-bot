import os
import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("DISCORD_TOKEN is missing from .env")

bot = discord.Client(intents=discord.Intents.default())
bot.run(token)