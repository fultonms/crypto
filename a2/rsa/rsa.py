import modular
import prime
import argparse

class RSA(object):
   def __init__(self, k=None, N=None, e=None, d=None):
      self.k = k
      self.N = N
      self.e = e
      self.d = d

   def keygen(self):
      print "Generating primes"
      p = prime.genPrime(self.k)
      q = prime.genPrime(self.k)
      print "Primes selected."
      self.N = p * q
      phi = (p-1) * (q-1)
      e = 100
      d = 0
      while True:
         g, x, y = modular.xgcd(e, phi)
         if g == 1:
            d = x
            break
         e += 1
      print "Keys selected"

      self.e = e
      self.d = modular.mod(d,phi)
      print "N=", self.N
      print "E=", self.e
      print "D=",  self.d

   @classmethod
   def load(cls,f):
      lines = f.readlines()
      N = int(lines[0].rstrip('\n'))
      e = int(lines[1].rstrip('\n'))
      d = int(lines[2].rstrip('\n'))
      return cls(None, N, e, d)
         

   def save(self, f):
      f.write(str(self.N) + '\n')
      f.write(str(self.e) + '\n')
      f.write(str(self.d) + '\n')
      f.close()
      
   def encrypt(self, m):
      return pow(ord(m), self.e, self.N)

   def decrypt(self, c):
      return chr(pow(c, self.d, self.N)) 

if __name__=='__main__':
   parser = argparse.ArgumentParser(description="")
   parser.add_argument('mode', metavar='mode', type=str, help='Encrypt(-e) or decrypt(-d).')
   parser.add_argument('inF', metavar='in', type=str, help='Path to the input file .')
   parser.add_argument('outF', metavar='out', type=str, help='Path to the output file.')
   parser.add_argument('-kf', required=False, help='A file containing the public keys.', nargs=1, type=str, metavar='IP', dest='kf')
   
   args = parser.parse_args()
   mode = args.mode
   inf = args.inF
   outf = args.outF
   keyFile = None
   if args.kf != None:
      keyFile = args.kf[0] 

   if keyFile != None:
      rsa = RSA.load(open(keyFile))
   else:
      rsa = RSA(64)
      rsa.keygen()
      rsa.save(open('keys.dat', 'w'))

   inl = open(inf).readlines()
   out = open(outf, 'w')
   if mode == 'e':
      for line in inl:
         for m in line:
            c = rsa.encrypt(m)
            out.write(str(c) + '\n')

   elif mode == 'd':
      if keyFile == None:
         print "Decrypting with newly generated keys? Nah..."
         exit(1)
      for line in inl:
         m = rsa.decrypt(int(line.rstrip('\n')))
         out.write(m)

   else:
      print "Bad mode!"


else:
   print 'Dont ever speak to me or my son ever again.'
