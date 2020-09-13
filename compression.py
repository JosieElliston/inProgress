def compress(n):
	guess1 = 1
	counter = 0
	while True:
		counter += 1
		guess1 = .5*(guess1+(2/guess1))
		print(guess1*10**counter)