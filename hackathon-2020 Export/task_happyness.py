from task import Task
import random
import discord
import asyncio
from stringtools import *


class Happyness(Task):



	######################################
	# Constructor
	def __init__(self):
		super().__init__()

		self.aliases = ["happy", "sad"]
		

	############################
	# use this task function
	async def start(self, msg, cli):
		
		
		# if this isn't for this task give up
		if (self.isAlias(msg.content) == False):
			#print(msg.content + " Not in " + str(self.aliases))
			return
		
		print("Running Happyness!")


		jokes = ["your a good person", "everythings fine", "your not a loser", "believe in yourself", "think happy thoughts"]
		
		await cli.sendMessage(random.choice(jokes))
			
		
		while True:
			
			more = (await cli.getResponse("Would you like another happy quote?")).content

			# if user wants another joke
			if (findWordString(more, "more") != -1 or findWordString(more, "another") != -1 or findWordString(more, "yes") != -1):

				await cli.sendMessage(random.choice(jokes))

		
			# if user wants no more jokes	
			else:
				await cli.sendMessage("Sorry to see you go")
				break

				