import elliptic

class ECEG(object):
   def __init__(self, curve, gen, pub, n):
      self.curve = curve
      self.gen = gen
      self.pub = pub
      self.n = n
   
   def save(self):
      pass

   @classmethod
   def load(cls, keyFile):
      lines = [line.strip() for line in keyFile.readlines()]
      assert len(lines) >= 5

      curve = elliptic.Curve(int(lines[0]), int(lines[1]), int(lines[2]))
      gen = curve.Point(int(lines[3].split(',')[0]), int(lines[3].split(',')[1]))
      pub = curve.Point(int(lines[4].split(',')[0]), int(lines[4].split(',')[1]))
      n = int(lines[5])

      return cls(curve, gen, pub, n)

   def encrypt(self, m):
      pass

   def decrypt(self, cipherFile): 
      message = list()
      lines = [line.strip() for line in cipherFile.readlines()]

      for line in lines:
         coords = line.split()
         y = self.curve.Point(int(coords[0]), int(coords[1]))
         halfMask = self.curve.Point(int(coords[2]), int(coords[3]))
         m = y - (halfMask * self.n)
         message.append(m)

      return message
         

   def __repr__(self):
        return 'EllipticElGamal(%r, %r, %r, %r)'%(self.curve, self.gen, self.pub, self.n)

if __name__ == '__main__':
   #print "Import this module, do not run it."
   instance = ECEG.load(open('pub.keys'))
   message = instance.decrypt(open('a4.cipher'))
   msgstr = ''
   for m in message:
      msgstr += chr(m[0])
   print msgstr
else:
   pass
