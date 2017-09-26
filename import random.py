import random

def checkGuess(guess, actual):
	if guess == actual:
		print("Correct!")
		return True
wordList = {
	'information' : 'It is the processed result of data' , 
	"population" : "The amount of ppl living in a place",
	"message" : "Giving out information" ,
	"random" : "No particular order"
}
randomWord, definition = random.choice(list(wordList.items()))

print("Hello. welcome to the guess game")
print("The definition of your word is: " + definition)
guess = input("Guess the word: ")
correct = False
while (correct == False):
	if (checkGuess(guess, randomWord) == True):
		break
	else:
		print("OLodo! Guess Again")
		anotherChance = input('Try a correct answer this time: ')
		if(checkGuess(anotherChance, randomWord) == True):
			break
