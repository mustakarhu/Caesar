
import string

class Caesar:

	listlower = list(string.ascii_lowercase)
	listupper = list(string.ascii_uppercase)

	def __init__(self,message:str,key:int=0):
		self.key = key
		self.message = message

	def changemessage(self):
		message = input('message input (press enter): ')
		self.message = message
	def changekey(self):
		while True:

			try:
				k = int(input('enter new key (1-25): '))
			
			except TypeError:
				print('please input a number')
				continue

			else:
				if k<0 or k>25:
					print('key value is not valid. Please input a number between 1 and 25')
				else:
					self.key = k
					print('new key is: ', self.key)
					break


	def encodemessage(self):
		output =''
		print('encoding message: '+self.message)
		for letter in self.message:
			
			if letter.lower() in self.listlower:
				idx = (self.listlower.index(letter.lower())+self.key)%26
				if letter.isupper():
					output +=self.listlower[idx].upper()
				else:
					output +=self.listlower[idx]

			else:
				output+=letter

		self.message = output
		print('encoded message: '+self.message)


	def decodemessage(self):
		output=''
		print('encoded message: '+self.message)
		for letter in self.message:		
			if letter.lower() in self.listlower:
				idx = (self.listlower.index(letter.lower())+(26-self.key))%26
				if letter.isupper():
					output +=self.listlower[idx].upper()
				else:
					output +=self.listlower[idx]

			else:
				output+=letter
		self.message = output
		print("decoded message: "+self.message)


	def savemessage(self):
		pass



if __name__ =='__main__':

	message = input('welcome to Caesar Cypher app. \nPlease insert a message: ')
	caesar = Caesar(message, 1)
	while True:
		command = input('please select command: \n (I) input new message \n (E) encode \n (D) decode\n (S) save message \n (K) change key \n (B) exit \n:')
		if command.upper() == 'I':
			caesar.changemessage()
		elif command.upper() == 'E':
			caesar.encodemessage()
		elif command.upper() == 'D':
			caesar.decodemessage()
		elif command.upper() == 'S':
			caesar.savemessage()
		elif command.upper() == 'K':
			caesar.changekey()
		elif command.upper() == 'B':
			print('exiting program. Thank you')
			break
		else:
			continue
