import discord
import os
import sys
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))

@bot.command()
async def hello(ctx: commands.Context):
  await ctx.send("Hello, {0.author}!".format(ctx.message))

# Load the auth token from the environment variables.
token = os.environ.get("DISCORD_TOKEN")

if token == None:
  print("The Discord bot token should be set as an environment variable named `DISCORD_TOKEN`")
  sys.exit(1)

# Initialize and connect the bot.
bot.run(token)
