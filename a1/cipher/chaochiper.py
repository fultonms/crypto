from collections import deque
import argparse, sys

parser = argparse.ArgumentParser(description="Encrypt a plaintext file, or decrypt a ciphertext file using the Chaocipher.")
parser.add_argument('act', metavar='action', type=str, help='Defines the action to perform (encrypt or decrypt).')
parser.add_argument('alphabetFile', metavar='alphabets', type=str, help='Path to the alphabets file.')
parser.add_argument('textFile', metavar='text', type=str, help='Path to the plaintext to encrypt, or the ciphertext to decrypt.')

args = parser.parse_args()


def leftPermute(alphabet, zenith):
   alphabet = deque(alphabet)
   while alphabet[0] != zenith:
      alphabet.rotate(-1)

   nadir = alphabet[1]
   for i in range(1,13):
      alphabet[i] = alphabet[i+1]
   alphabet[13] = nadir
   return list(alphabet)

def rightPermute(alphabet, zenith):
   alphabet = deque(alphabet)
   while alphabet[0] != zenith:
      alphabet.rotate(-1)
   alphabet.rotate(-1)
   
   nadir = alphabet[2]
   for i in range(2, 13):
      alphabet[i] = alphabet[i+1]
   alphabet[13] = nadir
   return list(alphabet)

if __name__ == '__main__':

   if args.act[0].lower() == 'e':
      action = 'e'
   elif args.act[0].lower() == 'd':
      action = 'd'
   else:
      sys.exit()

   #define lists for the left and right alphabets.
   left= list()
   right = list()

   with open(args.alphabetFile, 'r') as aFile:
      lines = aFile.readlines()
      for char in lines[0]:
         if char != '\n':
            left.append(char)
      for char in lines[1]:
         if char != '\n':
            right.append(char)
   
   outText = ''

   with open(args.textFile, 'r') as text:
      for word in text:
         for char in word:
            if char == '\n' or char == ' ':
               continue
            if action == 'e':
               idx = [i for i, pt in enumerate(right) if pt == char][0]
               outText += left[idx]
               left = leftPermute(left, left[idx])
               right = rightPermute(right, right[idx])
               
            else:
               idx = [i for i, ct in enumerate(left) if ct == char][0]
               outText += right[idx]
               left = leftPermute(left, left[idx])
               right = rightPermute(right, right[idx])

   print outText 
