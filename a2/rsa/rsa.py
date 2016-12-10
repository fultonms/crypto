class RSA(object):
   def __init__(self, n, e, d):
      self.n = n
      self.e = e
      self.d = d
      pass

   @classmethod
   def load(cls, keyFile):
      lines = [line.strip() for line in keyFile.readlines()]
      assert len(lines) >= 2

      n = int(lines[0])
      e = int(lines[1])
      if len(lines)>2 : 
         d = int(lines[2])
      else: 
         d = None

      return cls(n, e, d) 

   def save(self, keyFile):
      pass

   def keygen(self):
      pass

   def encrypt(self, plainFile):
      cipher = list()
      lines= [line.strip() for line in plainFile.readlines()]
     
      cipher.append(pow(ord(' '), self.e,self.n))
      for line in lines:
         m = ord(line)
         c = pow(m, self.e, self.n)
         cipher.append(c)

      return cipher

   def decrypt(self, cipherFile):
      message = list()
      lines = [line.strip() for line in cipherFile.readlines()]
      
      for line in lines:
         c = pow(int(line), self.d, self.n)
         m = chr(c)
         message.append(m)

      return message

   def __repr__(self):
      return 'RSA(%r, %r, %r)'%(self.n, self.e, self.d)

if __name__=='__main__':
   instance = RSA.load(open('pub.keys'))
   cipher = instance.encrypt(open('alphabet.txt'))
   for c in cipher:
      print c
else:
   pass

