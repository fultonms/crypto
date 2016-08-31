import argparse

parser = argparse.ArgumentParser(description="Decrpyt a selection of text from a substitution cypher, with the provided key")
parser.add_argument('cryptFile', metavar='encrypted', type=str, help='Path to the encrpyted text')
parser.add_argument('keyFile', metavar='key', type=str, help='Path to the key file')

args = parser.parse_args()
key = dict()

with open(args.keyFile, 'r') as keyFile:
	content = keyFile.readlines()
	for line in content:
		parts = line.split()
		key[parts[0]] = parts[1]


with open(args.cryptFile, 'wr') as cryptFile:
	contents = cryptFile.read()
	for k, v in key.items():
		contents.replace(k,v)			
