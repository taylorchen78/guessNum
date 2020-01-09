import random

num = random.randint(1, 100)
bIsGuessRight = False
guessCount = 0

while bIsGuessRight == False:
	guessNum = input("Guess num: ")
	guessNum = int(guessNum)
	guessCount += 1
	if guessNum == num:
		print("Correct, total guess", guessCount, "count")
		bIsGuessRight = True
	elif guessNum > num:
		print("Number is smaller")
	else:
		print("Number is bigger")
