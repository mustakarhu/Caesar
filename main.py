from caesar import Caesar


def main():
	message = input('welcome to Caesar Cypher app. \nPlease insert a message: ')
	ccypher = Caesar(message, 1)
	while True:
		command = input('please select command: \n (I) input new message \n (E) encode \n (D) decode\n (S) save message \n (K) change key \n (B) exit \n:')
		if command.upper() == 'I':
			ccypher.changemessage()
		elif command.upper() == 'E':
			ccypher.encodemessage()
		elif command.upper() == 'D':
			ccypher.decodemessage()
		elif command.upper() == 'S':
			ccypher.savemessage()
		elif command.upper() == 'K':
			ccypher.changekey()
		elif command.upper() == 'B':
			print('exiting program. Thank you')
			break
		else:
			continue


if __name__ =='__main__':
	main()

