from random import randrange
from primeTest import isPrime
from gcd import gcd
from factor import factor



def generatesprivpubl(size):
	p = randrange(2**size, 2**(size+1))
	q = p+1
	while not isPrime(p):
		p = randrange(2**size, 2**(size+1))
	while not isPrime(q) or q == p:
		q = randrange(2**size, 2**(size+1))
	
	n = p*q
	
	totient = (p-1)*(q-1)
	e = randrange(2, totient)
	while gcd(e, totient) != 1:
		
		e = randrange(2, totient)
	
	for d in range(totient):
		if (e*d)%totient == 1:
			print(p, q, totient)
			return (n, e), d
		
	print("no valid private keys < totient")




def encript(m, publ):
	assert gcd(m, publ[0]) == 1
	assert m < publ[0]
	return (m^publ[1])%publ[0]


def decript(c, publ, priv):
	return (c^priv)%publ[0] #where is e



publ, priv = generatesprivpubl(7)

m = 100

c = encript(m, publ)

mPrime = decript(c, publ, priv)



print("publ =", str(publ), "priv =", str(priv), "m =", str(m), "c =", str(c), "mPrime =", str(mPrime), m == mPrime)