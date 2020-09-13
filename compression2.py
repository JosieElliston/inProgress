def frequency(string):
	dic = {}
	for letter in string:
		if not letter in dic:
			dic[letter] = 0
		dic[letter] += 1
	
	keys = sorted(dic.keys())
	vals = sorted(dic.values())
	dic2 = {}
	
	for val in vals:
		for key in keys:
			if dic[key] == val:
				dic2[key] = val
				del dic[key]
				keys = sorted(dic.keys())
	
	return dic2
	
def huffman(string):
	for letter in string:
		pass