class binary:
	def __init__(self, n, base):
		if base == 10:
			self.value = int(bin(n)[2:])
		if base == 2:
			self.value = int(n)
	def __add__(self, other):
		a = self.value
		b = other.value
		a = int(str(a), 2)
		b = int(str(b), 2)
		c = a + b
		return int(binary(c), 10)
	def __sub__(self, other):
		a = self.value
		b = other.value
		a = int(str(a), 2)
		b = int(str(b), 2)
		c = a - b
		return int(binary(c), 10)
	def __str__(self):
		return str(self.value)
	def __int__(self):
		return int(str(self.value))
	def timesTen(self):
		self.value = int(str(self.value) + "0")
	def singleMult(self, other):
		assert (len(str(self.value)) < 2) and (len(str(other.value)) < 2)
		return int(str(int(self.value and other.value)) + str(int(self.value or other.value)))


def karatsuba(n, m):
	if type(n) != binary:
		print("type isn't binary")
		n = binary(n, 10)
		m = binary(m, 10)
	if len(str(n)) < 2 and len(str(m)) < 2:
		return n.singleMult(m)
	
	nLen = len(str(n))
	mLen = len(str(m))
	nMid = nLen//2
	mMid = mLen//2
	
	a = binary(str(n)[:nMid], 2)
	b = binary(str(n)[nMid:], 2)
	c = binary(str(m)[:mMid], 2)
	d = binary(str(m)[mMid:], 2)
	
	ac = karatsuba(a, c)
	bd = karatsuba(b, d)
	third = karatsuba((a+b), (c+d)) - ac - bd
	
	for i in range((nLen - nMid)**2):
		ac.timesTen()
	for i in range(mMid):
		third.timesTen()
	
	return ac + bd + third
	


a = binary(10, 10)

b = binary(2, 10)