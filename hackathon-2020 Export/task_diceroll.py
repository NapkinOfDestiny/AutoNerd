from task import Task
import random
import discord
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient


class DiceRoll(Task):



	######################################
	# Constructor
	def __init__(self):
		super().__init__()

		self.aliases = ["diceroll", "roll", "rand number", "rolldice"]
		

	############################
	# use this task function
	async def start(self, msg, cli):
		
		
		# if this isn't for this task give up
		if (self.isAlias(msg.content) == False):
			#print(msg.content + " Not in " + str(self.aliases))
			return

		print("Running Dice!")
		

		await cli.sendMessage("Starting Dice Roll 🎲")
		
		
		max_ = None
		min_ = None
		badValues = True

		while badValues:

			badValues = False# default to good values

			max_ = (await cli.getResponse("What is your max dice value")).content

			await cli.sendMessage("Max is: " + str(max_))
			min_ = (await cli.getResponse(("What is your\n min dice value""\n"))).content
			await cli.sendMessage(("Min is: " + str(min_)))

			# if not good values go again@TODO this doesn't work for some reason?
			#if (max_ < min_):
			#	await cli.sendMessage("Thats not how min and max work.")
			#	badValues = True
			
			if (not(max_.isnumeric()) or not(min_.isnumeric())):
				await cli.sendMessage("Please use numbers.")
				badValues = True

			if (badValues):
				print("try again:")


		#roll_again = "yes"
		#if roll_again == "yes" or roll_again == "y":
		await cli.sendMessage("Rolling the 🎲...")

		

		# play dice roll sound
		cli.player.play(discord.FFmpegPCMAudio('sfx/RollDice.mp3'), after=lambda e: print('done', e))

		while cli.player.is_playing():
			print("Playing dice rolling sound!")
			await asyncio.sleep(1)
		cli.player.stop()

		await cli.sendMessage("You got....")

		rand=(random.uniform(int(min_), int(max_)))
		await cli.sendMessage((int(rand)))