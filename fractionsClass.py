from gcd import gcd

class fraction:
	
	def __init__(self, num, den):
		self.num = num
		self.den = den
		if int(self.num) == self.num:
			self.num = int(self.num)
		if int(self.den) == self.den:
			self.den = int(self.den)
	
	def __set__(self, name, val):
		pass
		
	def copy(self):
		return fraction(self.num, self.den)
	
	def __str__(self):
		"""
		if int(self.num) == self.num:
			self.num = int(self.num)
		if int(self.den) == self.den:
			self.den = int(self.den)
		"""
		return str(self.num) + "/" + str(self.den)
	
	def __float__(self):
		return self.num/self.den
	
	def __int__(self):
		return int(float(self))
	
	
	def __lt__(self, other):
		return float(self) < float(other)
	
	def __gt__(self, other):
		return float(self) > float(other)
	
	def __eq__(self, other):
		a = self.copy().reduce()
		b = other.copy().reduce()

		return a.num == b.num and a.den == b.den
	
	
	
	
	def reduce(self):
		
		try:
			a = 1/(self.num%1)
			self.num = self.num*a
			self.den = self.den*a
		except ZeroDivisionError:
			pass
		
		try:
			b = 1/(self.den%1)
			self.num = self.num*b
			self.den = self.den*b
		except ZeroDivisionError:
			pass
		
		c = gcd(self.num, self.den)
		self.num = int(self.num/c)
		self.den = int(self.den/c)






	
a = fraction(1,2)

b = fraction(3,2)

c = fraction(3.5, 7.5)

c.reduce()

print(a == b)