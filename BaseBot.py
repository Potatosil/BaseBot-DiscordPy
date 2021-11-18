import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="$")


@bot.event # This is For When The Bot Gets On
async def on_ready():
	print("The Bot Is Online, May the Force be with you")

@bot.command() # COG LOADER
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.reply(f"Successfully Loaded {extension}")
    																	# THE COG LOADER AND UNLOADER
@bot.command() # COG UNLOADER
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.reply(f"Successfully Unloaded {extension}")


@bot.command()  #Ping Command
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')	


for filename in os.listdir('./Cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run('TOKEN') # Fill Your Bot Token Here :)