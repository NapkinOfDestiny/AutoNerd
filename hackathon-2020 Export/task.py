from stringtools import *

class Task(object):
	

	#####################
	# Constructor 
	def __init__(self):
		self.aliases = [] # filled in children


	###################################################
	# return if the message is a alias for message
	def isAlias(self, text):
		
		if (len(text) == 0):
			return False
		
		# if its one of our aliases the true
		for alias in self.aliases:
			
			if (findWordString(text, alias) != -1):
				return True

		return False
	
	############################
	# use this task function
	async def start(self, origMsg, cli):
		print("override me!")



