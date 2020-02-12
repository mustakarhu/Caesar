
from caesar import Caesar
import random

commands = {"-h": 0, "-e":1, "-d":2,"-i": 3, "-k": 4, "-o":5}

def help():
	'''
	Helper function shows available commands
	'''

	print(""" 
		COMMANDS: 	-e: encode message 
					-d: decode message
				 	-h:help
		FUNCTIONS:  -i: input file name 
					-k: specify key (optional. Default value = 3) 
					-o: output file name (optional. Default value = "output.txt")

		example: main.py -e -f demo.txt -k 13 -o encrypted""")

def parser(params:list):
	'''
	Analyzes the inputs passed via arguments.
	input: 		argv -> input arguments
	output: 	function -> what to execute (encode, decode, helper)
			 	options -> files to be saved on, define key etc.
	'''
	function=-1
	outname="default.txt"
	inname=""
	keyname=random.seed()
	for i in range(1,len(params)):
		if params[i] in commands.keys():
			if(params[i]=="-h"):
				function = commands["-h"]
				break
			elif(params[i]=="-e"):
				function = commands["-e"]
			elif(params[i]=="-d"):
				function = commands["-d"]
			elif(params[i]=="-i"):
				inname = params[i+1]
			elif(params[i]=="-o"):
				outname = params[i+1]	
			elif(params[i]=="-k"):
				keyname = int(params[i+1])

	return function, inname, outname, keyname




def run(params):


	function, infile, outfile, key = parser(params) 

	if(function==0):
		return help()
	else:

		cypher = Caesar(key,infile,outfile) # initialize object 
		cypher.encode() if(function==1) else cypher.decode()

