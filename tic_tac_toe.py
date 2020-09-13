def display(moves):
	
	print(" _____")
	
	for i in range(9):

		
		print("|", end="")
		
		if i%3 == 2:
			ending = "newLine"
		else:
			ending = "sameLine"
		if ending == "newLine":
			print(str(i) + "\u0332" + "|")
		else:
			print(str(i) + "\u0332", end="")
	
	print(" _____")
	
	for i in range(9):
		
		print("|", end="")
		
		if i%3 == 2:
			ending = "newLine"
		else:
			ending = "sameLine"
		if moves[i] != 0:
			if ending == "newLine":
				print(moves[i] + "\u0332" + "|")
			else:
				print(moves[i] + "\u0332", end="")
		else:
			if ending == "newLine":
				print(" " + "\u0332" + "|")
			else:
				print(" " + "\u0332", end="")

def doPlayerRound(moves, XorO):
	temp = moves[:]
	while True:
		validMove = True
		move = input("Where would " + str(XorO) + " like to go: ")
		
		if move == "":
			validMove = False
		
		if validMove:
			try:
				move = int(move)
			except ValueError:
				validMove = False
			
		if validMove and move > 9:
			validMove = False
			
		if validMove and moves[move] != 0:
			validMove = False
			
		if validMove:
			break
		else:
			print("invalid move")
	
	temp[move] = XorO
	return temp
				
				
def gameOver(moves):
	for i in range(9):
		if i == 8:
			return True, "tie"
		if moves[i] == 0:
			break
	
	if moves[0:3] == ["x", "x", "x"]:
		return True, "x"
	if moves[2:5] == ["x", "x", "x"]:
		return True, "x"
	if moves[5:8] == ["x", "x", "x"]:
		return True, "x"
	if moves[0:3] == ["o", "o", "o"]:
		return True, "o"
	if moves[2:5] == ["o", "o", "o"]:
		return True, "o"
	if moves[5:8] == ["o", "o", "o"]:
		return True, "o"
	
	if [moves[0], moves[3], moves[6]] == ["x", "x", "x"]:
		return True, "x"
	if [moves[1], moves[4], moves[7]] == ["x", "x", "x"]:
		return True, "x"
	if [moves[2], moves[5], moves[8]] == ["x", "x", "x"]:
		return True, "x"
	if [moves[0], moves[3], moves[6]] == ["o", "o", "o"]:
		return True, "o"
	if [moves[1], moves[4], moves[7]] == ["o", "o", "o"]:
		return True, "o"
	if [moves[2], moves[5], moves[8]] == ["o", "o", "o"]:
		return True, "o"
	
	if [moves[0], moves[4], moves[8]] == ["x", "x", "x"]:
		return True, "x"
	if [moves[2], moves[4], moves[6]] == ["x", "x", "x"]:
		return True, "x"
	if [moves[0], moves[4], moves[8]] == ["o", "o", "o"]:
		return True, "o"
	if [moves[2], moves[4], moves[6]] == ["o", "o", "o"]:
		return True, "o"
	
	return False, 0
	



def main():
	vs = ""
	while not (vs == "c" or vs == "p"):
		vs = input("play against computer (c) or player (p): ")
	
	moves = [0,0,0,0,0,0,0,0,0]
	
	if vs == "p":
		XorO = "o"
		while True:
			display(moves)
			
			if XorO == "o":
				XorO = "x"
			else:
				XorO = "o"
			
			gameOverOut = gameOver(moves)
			if gameOverOut[0]:
				print("Game over", str(gameOverOut[1]), "wins") 
				break
			else:
				moves = doPlayerRound(moves, XorO)
			
			


	else:
		print("not implemented")
		return
	
	
	
		XorO = ""
		while not (XorO == "x" or XorO == "o"):
			XorO = input("start as x (x) or go second as o (o): ")
		
main()
