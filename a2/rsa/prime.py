import random, modular

def genOdd(bits):
   r = random.getrandbits(bits)
   if r%2 ==0:
      return r + 1
   return r

smallPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def isProbablyPrime(n, k):
    if n < 2: return False
    for p in smallPrimes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def genPrime(bit):
   p = 1
   while not isProbablyPrime(p, 1000):
      p = genOdd(bit)

   return p

if __name__ == '__main__':
   while True:
      print genPrime(2048)
