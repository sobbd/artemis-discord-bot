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

@bot.command()
async def ping(ctx):
  latency = bot.latency * 1000  
  await ctx.send(f'Pong! Latency: {latency:.2f}ms')

@bot.command()
async def userinfo(ctx):
    user = ctx.author
    username = user.name
    discriminator = user.discriminator
    user_id = user.id
    roles = [role.name for role in user.roles if role.name != "@everyone"]
    nickname = user.nick
    avatar_url = user.avatar_url
    joined_date = user.joined_at.strftime("%Y-%m-%d %H:%M:%S")
    creation_date = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    embed = discord.Embed(title="User Information", color=discord.Color.green())
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Username", value=username, inline=False)
    embed.add_field(name="Discriminator", value=discriminator, inline=False)
    embed.add_field(name="User ID", value=user_id, inline=False)
    embed.add_field(name="Roles", value=', '.join(roles), inline=False)
    embed.add_field(name="Nickname", value=nickname, inline=False)
    embed.add_field(name="Joined Date", value=joined_date, inline=False)
    embed.add_field(name="Creation Date", value=creation_date, inline=False)  
    await ctx.send(embed=embed)
    
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    server_name = guild.name
    member_count = guild.member_count
    server_owner = guild.owner
    creation_date = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
    verification_level = guild.verification_level.name
    server_icon = guild.icon_url
    embed = discord.Embed(title="Server Information", color=discord.Color.blue())
    embed.set_thumbnail(url=server_icon)
    embed.add_field(name="Server Name", value=server_name, inline=False)
    embed.add_field(name="Member Count", value=member_count, inline=False)
    embed.add_field(name="Server Owner", value=server_owner, inline=False)
    embed.add_field(name="Creation Date", value=creation_date, inline=False)
    embed.add_field(name="Verification Level", value=verification_level, inline=False)
    await ctx.send(embed=embed)

# Load the auth token from the environment variables.
token = os.environ.get("DISCORD_TOKEN")

if token == None:
  print("The Discord bot token should be set as an environment variable named `DISCORD_TOKEN`")
  sys.exit(1)

# Initialize and connect the bot.
bot.run(token)
