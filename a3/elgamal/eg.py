import modular

class ElGamal(object):
   def __init__(self, p, g, b, a):
      self.p = p
      self.g = g
      self.b = b
      self.a = a

   @classmethod
   def load(cls, keyFile):
      lines = [line.strip() for line in keyFile.readlines()]
      assert len(lines) >= 3
      p = int(lines[0])
      g = int(lines[1])
      b = int(lines[2]) 
      a = int(lines[3])

      return cls(p, g, b, a)
   
   def save(self, outFile):
      pass

   def keygen(self, k):
      pass
   
   def encrypt(self, plainFile):
      pass

   def decrypt(self, cipherFile):
      message  = list()
      lines = [line.strip() for line in cipherFile.readlines()]
   
      for line in lines:
         alpha, y = int(line.split(',')[0]), int(line.split(',')[1])
         m = (y * modular.modInv(pow(alpha, self.a, self.p), self.p)) % self.p
         message.append(m)

      return message

   def __repr__(self):
      return 'ElGamal(%r, %r, %r, %r)'%(self.p, self.g, self.b, self.a)

if __name__ == '__main__':
   instance = ElGamal.load(open('pub.keys'))
   message = instance.decrypt(open('a3.cipher'))
   msgstr = ''
   for m in message:
      msgstr += chr(m)
   print msgstr
   
else:
   pass
