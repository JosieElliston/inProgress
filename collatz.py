TEXT = open("collatz.txt", mode="w")

def itter(n):
	if n%2 == 0:
		return n/2
	else:
		return n*3+1



counter = 0
dictn = {1:0}
while True:
	counter += 1
	x = counter
	y = 0
	while not x in dictn:
		x = itter(x)
		y += 1
	y += dictn[x]
	dictn[counter] = y
	print(counter, y)
	TEXT.write(str(y) + "\n")