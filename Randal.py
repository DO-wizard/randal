import discord 
import numpy as np
from discord.ext import commands

intents = discord.Intents().all()
client=commands.Bot(command_prefix='-r', intents=intents)

@client.command()
async def andlist(ctx, *args):
	#return an argument randomly from a list of arguments
	participants=0
	for arg in args:
		participants+=1
	winner=np.random.randint(0, participants)
	await ctx.send('And the winner is... ' + args[winner])

@client.command()
async def andus(ctx):
	#return an argument randomly from active voice chat users
	voice_channel=client.get_channel(935724161576366094)
	member_names=[]
	for x in voice_channel.members:
		member_names.append(x.name)
	winner=np.random.randint(0, len(member_names))
	await ctx.send('And the winner is... ' + member_names[winner])


client.run('OTM1OTE2NTM2Njc2MzYwMzAy.YfFmMg.1rExlniVzbXhRYA91mIxCqr76vI')

