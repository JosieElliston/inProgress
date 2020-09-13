import datetime
from random import shuffle, randint



def bubble(listn):
	for x in range(len(listn)):
		for i in range(len(listn)-x-1):
			if listn[i] > listn[i+1]:
				listn[i], listn[i+1] = listn[i+1], listn[i]
	return listn



def bubbleRecu(listn, n=0, x=0):
	if n+1 == len(listn):
		if x == len(listn):
			return listn
		else:
			x += 1
			return bubbleRecu(listn, 0, x+1)
	if listn[n] > listn[n+1]:
		listn[n], listn[n+1] = listn[n+1], listn[n]
	return bubbleRecu(listn, n+1)

"""del listn[y] #swap to debug
	listn.insert(len(listn)-n, x)"""


def selection(listn, n=0):
	if n == len(listn):
		return listn
	x = max(listn[0:len(listn)-n])
	y = listn.index(x)
	
	listn[y], listn[len(listn)-n-1] = listn[len(listn)-n-1], listn[y]
	
	return selection(listn, n+1)

def selectionOther(listn, n=0):
	if n == len(listn):
		return listn
	x = max(listn[0:len(listn)-n])
	y = listn.index(x)
	
	del listn[y] #swap to debug
	listn.insert(len(listn)-n, x)
	
	return selectionOther(listn, n+1)

def selection2(listn):
	for n in range(len(listn)):
		biggest = 0
		for i in range(len(listn)-n):
			if listn[biggest] < listn[i]:
				biggest = i
		listn[biggest], listn[len(listn)-n-1] = listn[len(listn)-n-1], listn[biggest]
	return listn



def merge(list1, list2):
	if len(list1) > len(list2):
		list1, list2 = list2, list1
	output = []
	
	while list1 and list2:
		item1 = list1[0]
		item2 = list2[0]
		if item1 < item2:
			output.append(item1)
			del list1[0]
		else:
			output.append(item2)
			del list2[0]
	
	for item in list2:
		output.append(item)
	for item in list1:
		output.append(item)

	return output



def mergeSort(listn):
	if len(listn) < 2:
		return listn
	else:
		mid = int(len(listn)/2)
		list1 = mergeSort(listn[:mid])
		list2 = mergeSort(listn[mid:])
		output = merge(list1, list2)
		return output



def quicksort(listn):
	
	lenlist = len(listn)
	
	if lenlist < 2:
		return listn
	
	pivotIndex = randint(0, lenlist-1)
	pivot = listn[pivotIndex]
	
	listn[pivotIndex], listn[0] = listn[0], listn[pivotIndex]
	
	small = []
	mid = []
	big = []
	
	
	for element in listn:
		if element < pivot:
			small.append(element)
		
		elif element == pivot:
			mid.append(element)

		else:
			big.append(element)


	listn = quicksort(small) + mid + quicksort(big)
	
	return listn

def quickInPlace(listn, low = 0, high = -1):
	pass









"""

listn = []
for i in range(10):
	listn.append(i)
shuffle(listn)

print(listn)
print(quicksort(listn))
"""


def test(sort, times, length):
	
	
	output = []
	for i in range(times):
		listn = []
		for i in range(length):
			listn.append(i)
		shuffle(listn)
		a = datetime.datetime.now()
		sort(listn)
		b = datetime.datetime.now()
		output.append((b-a).microseconds)
	return sum(output)/len(output)
		

#print("bubble took         ", test(bubble, 100, 100), "on average")
#print("selection took      ", test(selection, 100, 100, "on average")
#print("selectionOther took ", test(selectionOther, 100, 100), "on average")
#print("selection2 took     ", test(selection2, 100, 100), "on average")
print("merge took          ", test(mergeSort, 10000, 100), "on average")
print("quicksort took      ", test(quicksort, 10000, 100), "on average")
#print("native took         ", test(sorted, 100, 100), "on average")
