import datetime
from random import shuffle



def bubble(listn):
	for x in range(len(listn)):
		for i in range(len(listn)-1):
			if listn[i] > listn[i+1]:
				listn[i], listn[i+1] = listn[i+1], listn[i]
	return listn
		
		

listn = []
for i in range(100):
    listn.append(i)
shuffle(listn)



output = []
for i in range(1000):
	a = datetime.datetime.now()
	bubble(listn)
	b = datetime.datetime.now()
	output.append((b-a).microseconds)
print("Bubble took", str(sum(output)/len(output)), "on average")