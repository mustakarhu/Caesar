# Python Caesar cypher implementation

## About
This example is a simple implementation of the Caesar's cipher also known as substitution cipher which is one of the simplest and earliest implementations of cryptography. 

## Usage

The function has two main functions: Encrypt and Decrypt. 
The user specifies the key and the input file and the output if not specified is saved to a default file ("output.txt").

Examples:

Encoding a file named "demo.txt" with a key = 1000 and saving the code to a file named "encoded.txt"
'''
$python main.py -e -i demo.txt -k 1000 -o encoded.txt 
'''

Decoding a file with the key = 12 and saving the code to a file named "decoded.txt".
'''
$python main.py -d -i encoded.txt -k 12 -o decoded.txt 
'''

Since the Caesar cypher rotates over up to 26 different characters, the key is calculated using the modulo of the input key, therefore `1000 mod(26) = 12 mod(26)` the encoded text will be decoded using a different key.

## Future work

- Add brute force through frequency analysis
- Other substitution ciphers such as ROT-13 or Autokey.
