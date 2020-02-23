from task import Task
import random
import discord
import asyncio
import requests
import sys, random
import numpy as np 
import math 
from PIL import Image 

class AsciiArtify(Task):

	# 70 levels of gray 
	gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

	# 10 levels of gray 
	gscale2 = '@%#*+=-:. '

	######################################
	# Constructor
	def __init__(self):
		super().__init__()

		self.aliases = ["ascii this", "asciify this", "cooler", "improve this image", "beutify"]
		
	
	@staticmethod
	def getAverageL(image): 
	
		""" 
		Given PIL Image, return average value of grayscale value 
		"""
		# get image as numpy array 
		im = np.array(image) 
	
		# get shape 
		w,h = im.shape 
	
		# get average 
		return np.average(im.reshape(w*h)) 
	
	@staticmethod
	def covertImageToAscii(fileName, cols, scale, maxCharacters, moreLevels): 
		""" 
		Given Image and dims (rows, cols) returns an m*n list of Images  
		"""
		# declare globals 
		global gscale1, gscale2 
	
		# open image and convert to grayscale 
		image = Image.open(fileName).convert('L') 
	
		# store dimensions 
		W, H = image.size[0], image.size[1] 
		print("input image dims: %d x %d" % (W, H)) 

		
		# compute width of tile 
		w = W/cols 
	
		# compute tile height based on aspect ratio and scale 
		h = w/scale 

		# compute number of rows 
		rows = int(H/h) 


		if (int(rows*cols) > maxCharacters):
			
			return
			'''@TODO this doesn't work as intended
			r = math.sqrt(rows * rows + cols * cols)

			# scale back width and length evenly so they hit max just barely
			rows = (rows/r * maxCharacters)/rows
			cols = (cols/r * maxCharacters)/cols
			
	
			print("New Tile Dimensions W:" + str(cols) + "\t H:" + str(rows))
			# if we c an't evenly scale the image to make it fit the asci limit then give up
			if (rows <= 0 or cols <= 0):
				print("Unconvertable Image")
				return
			
			image = image.resize((int(W * cols) , int(H * rows)))

			rows = int(rows)
			cols = int(cols)
			
			# store dimensions 
			W, H = image.size[0], image.size[1] 
			print("changing input image dims to: %d x %d" % (W, H)) 

			w = W/cols 
			h = w/scale 	

			# compute number of rows 
			#rows = int(H/h) 
			'''
			

		print("cols: %d, rows: %d" % (cols, rows)) 
		print("tile dims: %d x %d" % (w, h)) 
	
		# check if image size is too small 
		if cols > W or rows > H: 
			print("Image too small for specified cols!") 
			exit(0) 
	
		# ascii image is a list of character strings 
		aimg = [] 
		# generate list of dimensions 
		for j in range(rows): 
			y1 = int(j*h) 
			y2 = int((j+1)*h) 
	
			# correct last tile 
			if j == rows-1: 
					y2 = H 
	
			# append an empty string 
			aimg.append("") 
	
			for i in range(cols): 
			
					# crop image to tile 
					x1 = int(i*w) 
					x2 = int((i+1)*w) 
	
					# correct last tile 
					if i == cols-1: 
						 x2 = W 
	
					# crop image to extract tile 
					img = image.crop((x1, y1, x2, y2)) 
	
					# get average luminance 
					avg = int(AsciiArtify.getAverageL(img)) 
	
					# look up ascii char 
					if moreLevels: 
						sval = AsciiArtify.gscale1[int((avg*69)/255)] 
					else: 
						gsval = AsciiArtify.gscale2[int((avg*9)/255)] 
	
					# append ascii char to string 
					aimg[j] += gsval 
	
		# return txt image 
		return aimg 

	############################
	# use this task function
	async def start(self, msg, cli):
		
		
		# if this isn't for this task give up
		if (self.isAlias(msg.content) == False):
			#print(msg.content + " Not in " + str(self.aliases))
			return

		print("Running Asciiartify!")
		
		
		for attachment in msg.attachments: 
			print("Found Attachment @url:" + attachment.url)



			myfile = requests.get(attachment.url)
			open('temp/temp.file', 'wb').write(myfile.content)


  
	
	
			# gray scale level values from:  
			# http://paulbourke.net/dataformats/asciiart/ 
	
			
		

			# set scale default as 0.43 which suits 
			# a Courier font 
			scale = 0.43


			# set cols 
			cols = 80


			print('generating ASCII art...') 
			# convert image to ascii txt 
			aimg = AsciiArtify.covertImageToAscii("temp/temp.file", cols, scale, 1992, False) 

			# write each row as line
			result = "```\n"
			for row in aimg: 
				result += "|" + row + "|\n"
			
			result += "\n```"
			print("CharLength:" + str(len(result)))

			await cli.sendMessage(result) 

			