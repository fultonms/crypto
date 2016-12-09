import argparse

parser = argparse.ArgumentParser(description="Decrpyt a selection of text from a substitution cypher, with the provided key")
parser.add_argument('cryptFile', metavar='encrypted', type=str, help='Path to the encrpyted text')
parser.add_argument('keyFile', metavar='key', type=str, help='Path to the key file')

args = parser.parse_args()
key = dict()
