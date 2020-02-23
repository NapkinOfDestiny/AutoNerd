from task import Task
import random
import discord
import asyncio
import threading 
from stringtools import *


class Timer(Task):



	######################################
	# Constructor
	def __init__(self):
		super().__init__()

		self.aliases = ["timer", "remind"]
		self.done = True
	
	

	############################
	# use this task function
	async def start(self, msg, cli):
		
		
		# if this isn't for this task give up
		if (self.isAlias(msg.content) == False):
			#print(msg.content + " Not in " + str(self.aliases))
			return
		
		print("Running Timer!")

		
			
		
		# get numeric input from user for time length
		waitTime = None
		while True:
			waitTime = (await cli.getResponse("How many seconds?")).content

			if not(waitTime.isnumeric()):
				await cli.sendMessage("Please enter a number.")
			else:
				break

		await asyncio.sleep(float(waitTime)) # wait for the specified time


		await cli.sendMessage("Timer Done!")

		cli.player.play(discord.FFmpegPCMAudio('sfx/alarm.wav'), after=lambda e: print('done', e))
		while cli.player.is_playing():
			print("Playing alarm sound!")
			await asyncio.sleep(1)#@TODO does this do anthing because its the end?

		cli.player.stop()
		
	
		

		
		
		

		
		

				