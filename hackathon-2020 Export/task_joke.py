from task import Task
import random
import discord
import asyncio
from stringtools import *


class Joke(Task):



	######################################
	# Constructor
	def __init__(self):
		super().__init__()

		self.aliases = ["tell me a joke", "joke?", "jokes", "say something funny", "make me laugh"]
		

	############################
	# use this task function
	async def start(self, msg, cli):
		
		
		# if this isn't for this task give up
		if (self.isAlias(msg.content) == False):
			#print(msg.content + " Not in " + str(self.aliases))
			return
		
		print("Running Joke!")


		jokes = [ "I'm reading a book about anti-gravity. It's impossible to put down!", "Why Can't You Trust Atoms?They make up everything.", "What do you call someone with no body and no nose? Nobody knowsNE."
				,"The fattest knight at King Arthur’s round table was Sir Cumference. He acquired his size from too much pi.","Why did the invisible man turn down the job offer? He couldn't see himself doing it.",
				"What's the best part about living in Switzerland? I don't know, but the flag is a big plus."
				"What do you call a dog that can do magic? A Labracadabrador.","I used to have a job at a calendar factory but I got the sack because I took a couple of days off.","Why do bicycles fall over?Because they are two-tired!","Why do dragons sleep during the day? So they can fight knights!","Were you long in the hospital?No, I was the same size I am now!","Why couldn't the pirate play cards? Because he was sitting on the deck!","Why can't your nose be 12 inches long? Because then it would be a foot!","What makes the calendar seem so popular?Because it has a lot of dates!"]
		
		await cli.sendMessage(random.choice(jokes))
			
		
		while True:
			
			more = (await cli.getResponse("Would you like another joke?")).content

			# if user wants another joke
			if (findWordString(more, "more") != -1 or findWordString(more, "another") != -1 or findWordString(more, "yes") != -1):

				await cli.sendMessage(random.choice(jokes))

		
			# if user wants no more jokes	
			else:
				await cli.sendMessage("Sorry to see you go")
				break

				