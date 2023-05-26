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
async def ping(ctx: commands.Context):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')

@bot.command()
async def userinfo(ctx: commands.Context):
    user: discord.Member = ctx.author
    username: str = user.name
    discriminator: str = user.discriminator
    user_id: int = user.id
    roles: list[str] = [role.name for role in user.roles if role.name != "@everyone"]
    nickname: str = user.nick
    avatar_url: str = user.avatar_url
    joined_date: str = user.joined_at.strftime("%Y-%m-%d %H:%M:%S")
    creation_date: str = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
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
async def serverinfo(ctx: commands.Context):
    guild: discord.Guild = ctx.guild
    server_name: str = guild.name
    member_count: int = guild.member_count
    server_owner: discord.Member = guild.owner
    creation_date: str = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
    verification_level: str = guild.verification_level.name
    server_icon: str = guild.icon_url
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

if token is None:
    print("The Discord bot token should be set as an environment variable named `DISCORD_TOKEN`")
    sys.exit(1)

# Initialize and connect the bot.
bot.run(token)
