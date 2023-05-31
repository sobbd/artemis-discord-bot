import discord
import os
import sys
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="A general-purpose bot, created for learning Python and as a collaborative project."))

# Load the auth token from the environment variables.
token = os.environ.get("DISCORD_TOKEN")

if token is None:
  print("The Discord bot auth token should be set as an environment variable named `DISCORD_TOKEN`")
  sys.exit(1)

@bot.command()
async def hello(ctx: commands.Context):
  await ctx.send("Hello, {0.author}!".format(ctx.message))

@bot.command()
async def ping(ctx: commands.Context):
  # The latency is given in seconds. Multiply by 1000 to convert
  # it into milliseconds (ms).
  latency = bot.latency * 1000

  await ctx.send(f"Pong! Latency: {latency:.2f}ms.")

@bot.command()
async def userinfo(ctx: commands.Context):
  # Use a for comprehension to collect all the roles of the author,
  # excluding the `@everyone` role which would not be informative.
  roles: list[str] = [role.name for role in ctx.author.roles if role.name != "@everyone"]

  joined_date: str = ctx.author.joined_at.strftime("%Y-%m-%d %H:%M:%S")
  creation_date: str = ctx.author.created_at.strftime("%Y-%m-%d %H:%M:%S")
  embed = discord.Embed(title="User information", color=discord.Color.green())

  embed.set_thumbnail(url=ctx.author.avatar)
  embed.add_field(name="Username", value=ctx.author.name, inline=False)
  embed.add_field(name="Discriminator", value=ctx.author.discriminator, inline=False)
  embed.add_field(name="User ID", value=ctx.author.id, inline=False)
  embed.add_field(name="Roles", value=", ".join(roles), inline=False)
  embed.add_field(name="Nickname", value=ctx.author.nick, inline=False)
  embed.add_field(name="Joined date", value=joined_date, inline=False)
  embed.add_field(name="Creation date", value=creation_date, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx: commands.Context):
  creation_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
  embed = discord.Embed(title="Server information", color=discord.Color.blue())

  embed.set_thumbnail(url=ctx.guild.icon)
  embed.add_field(name="Server name", value=ctx.guild.name, inline=False)
  embed.add_field(name="Member count", value=ctx.guild.member_count, inline=False)
  embed.add_field(name="Server owner", value=ctx.guild.owner.mention, inline=False)
  embed.add_field(name="Creation date", value=creation_date, inline=False)
  embed.add_field(name="Verification level", value=ctx.guild.verification_level.name, inline=False)
  await ctx.send(embed=embed)

@bot.command(name="create_project")
async def create_project_embed(ctx: commands.Context, name: str, thumbnail_url: str, description: str, tech_stack: str, expertise_level: str, github_url: str):
  embed = discord.Embed(title=name)

  embed.set_thumbnail(url=thumbnail_url)
  embed.add_field(name="Description", value=description, inline=False)
  embed.add_field(name="Tech stack", value=tech_stack, inline=False)
  embed.add_field(name="Recommended expertise level", value=expertise_level, inline=False)
  embed.add_field(name="GitHub URL", value=github_url, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def announce(ctx: commands.Context, message: str):
  if ctx.guild is None:
    await ctx.reply("This command is only usable within a server.")

    return
  elif ctx.author.bot or not ctx.author.guild_permissions.administrator:
    await ctx.reply("This command is only available to guild administrators!")

    return

  # Attempt to delete the triggering message for convenience.
  try:
    await ctx.message.delete()
  except:
    pass

  await ctx.send(f"@everyone {message}")

@bot.command()
async def github(ctx: commands.Context):
  await ctx.reply("https://github.com/sobbd/artemis-discord-bot")

@bot.command()
async def clear(ctx: commands.Context, amount: int):
  if ctx.guild is None:
    await ctx.reply("This command is only usable within a server.")

    return
  elif ctx.author.bot or not ctx.author.guild_permissions.administrator:
    await ctx.reply("This command is only available to server administrators!")

    return
  
  if amount <= 0:
    await ctx.reply("Please enter at least one message to delete.")

    return

  async for message in ctx.channel.history(limit=amount + 1):
    await message.delete()

# Initialize and connect the bot.
bot.run(token)
