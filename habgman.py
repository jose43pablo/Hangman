def gamePlay(secretWord):
	failedGuesses = 0
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	guess = ""
	displayWord = getDisplayWord(secretWord)
	gameOver = False

	while not gameOver:
		invalidInput = True
		while invalidInput:
			print("Jugador", Player, end = "")
			guess = input(", adivina una letra: ").upper()
			if len(guess) > 1 or guess not in alphabet:
				print("Adivinaste una letra!. Intenta de nuevo.")
			else:
				invalidInput = False
		if guess in secretWord:
			for i in range(len(secretWord)):
				if secretWord[i] == guess:
					displayWord[i] = guess
			printWord(displayWord)
			if "_" not in displayWord:
				print("Jugador", Player, " GANASTE!")
				gameOver = True
		else:
			failedGuesses += 1
			print("No le atinaste! Intenta de nuevo.")
			print("Estatus del ahorcado: ", end = "")

			if failedGuesses == 1:
				print("O")
			elif failedGuesses == 2:
				print("O-")
			elif failedGuesses == 3:
				print("O__")
			elif failedGuesses == 4:
				print("O-<")
			elif failedGuesses == 5:
				print("O+<")
			elif failedGuesses == 6:
				print("AHORCADO!")
				gameOver = True
			print(" Intentos restantes:", 6-failedGuesses)

			printWord(displayWord)
							
def printWord(displayWord):
	word = ""
	for i in range(len(displayWord)):
		word += displayWord[i]
	print()
	print("Progreso: ", word)

def getDisplayWord(secretWord):
	displayWord = []
	for i in range(len(secretWord)):
		if secretWord[i] in alphabet:
			displayWord.append("_")
		else:
			displayWord.append(secretWord[i])
	return displayWord

def main():
	global Player
	global alphabet
	Player = 1
	secretWord = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"		
	Continue = True

	while Continue:		
		if Player == 1:
			print()
			secretWord = input("Jugador uno, ingresa tu palabra secreta: ").upper()
			for i in range(50):
				print()
			Player = 2
			print("Jugador 2  Atinale a la palabra del Jugador uno")
			gamePlay(secretWord)
		elif Player == 2:
			print()
			secretWord = input("Jugador dos, ingresa tu palabra secreta: ").upper()
			for i in range(50):
				print()
			Player = 1
			print("Jugador 1 Atinale a la palabra del Jugador dos")
			gamePlay(secretWord)
		quit = input("Quieres salir? (Si/No): ").upper()
		if quit == "SI" or quit == "S" or quit=='s':
			Continue = False
	print()
	print("MUCHAS GRACIAS POR JUGAR AHORCADO!")

main()