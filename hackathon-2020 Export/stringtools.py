# misc String Functions

##########################################################################################
# finds if there is target surounded by whitespace or nothing in [start, end) of message.
# returns -1 for no target and the index of the first letter of target if their is
def findWordString(message, target, start=0, end=None):
		
	message = message.lower()
	target = target.lower()
	
	# if no end then set it to the end by default
	if (end == None):
		end = len(message)
		
	loca = message.find(target, start, end)


	# if target doesn't exist period then give up
	if (loca == -1):
		return -1

	# while the target can still fit in the message string 
	while loca < end - len(target) +1:
			
		# if target doesn't exist period then give up
		if (loca == -1):
			return -1

		
			
		# if not existing in list then assume its a space
		before = None
		if (loca -1 < 0):
			before = ' '
		else:
			before = message[loca -1]


		afterIndex = loca + len(target)
		after = None

		if (afterIndex >= end):
			after = ' '
		else:
			after = message[afterIndex]

		#print("'" + before + "'" + target + "'" + after + "'")
			
		# are before and after space, if so this is a valid loca
		if (before.isspace() and after.isspace()):
			return loca

		# jump to next instance of target because this one wasn't surrounded by space
		loca = message.find(target, loca + 1, end)

