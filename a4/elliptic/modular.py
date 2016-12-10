def mod(x, m):
   a = x % m
   if a < 0:
      a += m
   return a
   
def modInv(a, m):
   if a < 0: a += m
   g, x, y = xgcd(a, m)
   if g != 1:
      raise Exception('modular inverse doesnt exist')
   else:
      return mod(x, m)

def xgcd(a, b):
   if a == 0:
      return (b, 0, 1)
   else:
      g, y, x = xgcd(b %a, a)
      return (g, x- (b // a) * y, y)


if __name__ =='__main__':
   print "This module should not be run as main"
else:
   pass
