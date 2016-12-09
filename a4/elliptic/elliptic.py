import modular

class Curve(object):
   def __init__(self, a, b, q):
      self.a = a
      self.b = b
      self.q = q

   class Point(object):
      def __init__(self, curve, x, y):
         self.curve = curve
         
         if x is None and y is None:
            self.x = None
            self.y = None
         else:
            self.x = x % curve.q
            self.y = x % curve.q

      def _getX(self):
         return self.x

      def _getY(self):
         return self.y

      def _setX(self, x):
         if x is None:
            self.x = None
         else:
            self.x = x % self.curve.q

      def _setY(self, y):
         if y is None:
            self.y = None
         else:
            self.y  = y % self.curve.q

      x = property(_getX, _setX)
      y = property(_getY, _setY)

      @property
      def curve(self):
         self.curve

      def isInfinity(self):
         return self.x is None and self.y is None

   def __add__(self, 


def isPointInfinity(P):
   x, y = P
   if x == None and y == None:
      return True
   else:
      return False

def ellipticAdd(P, Q, a, q):
   Z = None

   if isPointInfinity(P):
      Z = Q
   elif isPointInfinity(Q):
      Z = P
   else:
      x1, y1 = P
      x2, y2 = Q

      if not modEq(x1, x2, q):
         m = mod((y2-y1) * modInv((x2-x1), q), q)
         c = mod(y1- (m * x1),q)

         x3 = mod(pow(m, 2) - (x1+x2), q)
         y3 = mod((m* x3) + c, q)
         Z = (x3, mod(q-y3, q))
      elif modEq(x1, x2, q) and modEq(y1, -y2, q):
         Z = (None, None)
      elif modeq(x1, x2, q) and modEq(y1, y2, q):
         m = mod(((3 * pow(x1,2)+ a) * modInv(2*y1, q)), q)
         x3 = mod((pow(m,2) - 2*x1, q))
         y3 = mod((y1 + m*(x3-x1)), q)
         Z = (x3, mod(q-y3, q))
         
      else:
         raise ValueError("The points shoudl fit into one of these three cases")

   return Z
   
def ellipticSub(P, Q, a, q):
   x, y = Q
   return ellipticAdd(P, (x, mod(-y, q)), a, q)

def ellipticMult(n, P, a, q):
   if n == 0:
      return (None, None)
   else:
      if n % 2 == 0:
         return ellipticMult(2, ellipticMult(n/2, P, a, q), a, q)
      else:
         return ellipticAdd(P, ellipticMult(n-1, P, a, q), a,  q)

def isPointInfinity(P):
   x, y = P
   if x == None and y == None:
      return True
   else:
      return False

if __name__== '__main__':
   #print "This module must be imported, not run as main."
   print decrypt((12, 2), (32, 32), 4, 4, 43)
else:
   pass
