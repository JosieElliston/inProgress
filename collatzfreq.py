outputText = open("collatzfreq.txt", mode="w")

def itter(n):
	if n%2 == 0:
		return n/2
	else:
		return n*3+1

content = []

counter = 0
dictn = {1:0}
for i in range(2000):
	counter += 1
	x = counter
	y = 0
	while not x in dictn:
		x = itter(x)
		y += 1
	y += dictn[x]
	dictn[counter] = y
	content.append(y)
	
		
print(content)

for i in range(max(content)):
	outputText.write(str(i) + " " + str(content.count(i)) + "\n")


	
outputText.close()