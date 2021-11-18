import discord
from discord.ext import commands

class ExampleCog(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("ExampleCog Is Ready")

	@commands.command()  #Hello Command
	async def hello(self, ctx):
		await ctx.send(f'Hey my Man Hope You Enjoy Here!')


	
def setup(client):
	client.add_cog(ExampleCog(client))
