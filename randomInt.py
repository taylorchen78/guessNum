import random

start = input("Please choose start num: ")
end = input("Please choose end num: ")
start = int(start)
end = int(end)

num = random.randint(start, end)
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
