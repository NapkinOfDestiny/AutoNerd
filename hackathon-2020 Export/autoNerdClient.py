import discord
import sys
import os
from task_diceroll import DiceRoll
from task_joke import Joke
from task_asciiArtifi import AsciiArtify
from task_timer import Timer
from task_happyness import Happyness


class MyClient(discord.Client):


	#################
	# Constuctor
	def __init__(self):
		super().__init__()


		# load tasks
		self.tasks = []

		self.tasks.append(DiceRoll())
		self.tasks.append(Joke())
		self.tasks.append(AsciiArtify())
		self.tasks.append(Timer())
		self.tasks.append(Happyness())
		self.channel = None
		self.tts = False# do text to speach


	#######################################
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))


		# find channel called nerdbot by name, ideally this should be done by id
		for guild in client.guilds:
			for channel in guild.channels:
				if (channel.name == "nerdbot"):
					self.channel = channel

		self.player = None

		


	#################################################
	async def on_message(self, message):
	   
		# if its from ourselves or its not our channel then quit
		if (message.author == client.user or self.channel == None or self.channel != message.channel):
			return
		
		print('<Message from {0.author}: {0.content}'.format(message))



		# if user wants to restart do that
		if  (message.content == "restart"):
			await message.channel.send("Restarting...")

			os.system("python autoNerdClient.py")# start new
			sys.exit() # end ucrretn

		# if user wants to call client and is in the correct channel to do things wait for new msg
		if  (message.content.startswith('heynerd')):
			
			# configure voice chat to match authors channel
			if (message.author.voice != None and (self.player == None or self.player.channel != message.author.voice.channel)):
				print("Connecting to audio channel " + message.author.voice.channel.name)
				self.player = await message.author.voice.channel.connect()


			await message.channel.send("Yes?")

			msg = await self.getResponse()
		

			for task in self.tasks:
				await task.start(msg, self)

			await message.channel.send("Bye")

			
	

	####################################
	# sends a message!
	async def sendMessage(self, msg):

		print("Sending>'" + str(msg) + "'")
		await self.channel.send(msg, tts=self.tts)


	#######################################
	# waits for a response in the channel
	async def getResponse(self, msg=None):
		
		if (msg != None):
			await self.sendMessage(msg)

		def check(m):
			return (m.channel == self.channel and m.author != client.user)

		return await client.wait_for('message', check=check)





client = MyClient()
client.run('TOKEN_HERE')