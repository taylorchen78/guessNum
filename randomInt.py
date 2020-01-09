import random

num = random.randint(1, 100)
bIsGuessRight = False

while bIsGuessRight == False:
	guessNum = input("Guess num: ")
	guessNum = int(guessNum)
	if guessNum == num:
		print("Correct")
		bIsGuessRight = True
	elif guessNum > num:
		print("Number is smaller")
	else:
		print("Number is bigger")
