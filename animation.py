from time import sleep



def display(x, y):
	for i in range(10-y):
		print()
	for i in range(x):
		print(" ", end = "")
	print("o")
	for i in range(y):
		print()
	print("‾‾‾‾‾‾‾‾‾‾‾")
	
	
x = 0
y = 0
yvel = 0
xvel = 0

while True:
	
		
	if y < 1:
		yvel = 4
	else:
		yvel -= 1
	
	if x < 1:
		xvel = 1
	
	if x > 10:
		xvel = -1
	
	x += xvel
	y += yvel
	
	sleep(.2)
	display(x, y)
	
	
	#print(x, y, xvel, yvel)
	
		
	