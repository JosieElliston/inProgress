def farey(n):
	assert 0<n<1
	
	epsilon = .1**15
	lowNum = 0
	lowDen = 1
	highNum = 1
	highDen = 1
	
	while True:
		guessNum = lowNum + highNum
		guessDen = lowDen + highDen
		lowRat = lowNum/lowDen
		highRat = highNum/highDen
		guessRat = guessNum/guessDen
		if abs(n-(guessRat)) < epsilon:
			return guessNum, guessDen
		
		if n < guessRat:
			highNum = guessNum
			highDen = guessDen
		else:
			highNum = guessNum
			highDen = guessDen
			
def farey2(n):
	assert 0 < n < 1
	
	ln = 0
	ld = 1
	hn = 1
	hd = 1
	
	while True:
		
		gn = ln + hn
		gd = ld + hd
		gf = gn/gd
		
		if gf == n:
			return gn, gd
		
		elif n < gf:
			hn = gn
			hd = gd
			
		elif gf < n:
			ln = gn
			ld = gd
		
		#print((ln, hn, ln/ld), (hn, hd, hn/hd), (gn, gd, gf))
