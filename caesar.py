import string

class Caesar:

	listlower = list(string.ascii_lowercase)
	listupper = list(string.ascii_uppercase)

	def __init__(self, init_key:int, init_readfile:str, init_writefile:str):
		self.key = init_key
		self.input_file= init_readfile
		self.output_file = init_writefile
		

	def encode(self):
		
		try:
			in_file = open(self.input_file,"r")
			out_file = open(self.output_file,"w")
			for line in in_file:
				encoded_line = ""
				for letter in line:
					if letter.lower() in self.listlower:
						idx = (self.listlower.index(letter.lower())+self.key)%26
						if letter.isupper():
							encoded_line +=self.listlower[idx].upper()
						else:
							encoded_line +=self.listlower[idx]
					else:
						encoded_line+=letter

				out_file.write(encoded_line)

		except OSError:
			print(f"file {self.input_file} could not be opened")


	def decode(self):
		try:
			in_file = open(self.input_file,"r")
			out_file = open(self.output_file,"w")
			for line in in_file:
				decoded_line=""
				for letter in line:		
					if letter.lower() in self.listlower:
						idx = (self.listlower.index(letter.lower())+(26-self.key))%26
						if letter.isupper():
							decoded_line +=self.listlower[idx].upper()
						else:
							decoded_line +=self.listlower[idx]
					else:
						decoded_line+=letter
				out_file.write(decoded_line)

		except OSError:
			print(f"file {self.input_file} could not be opened")
		
