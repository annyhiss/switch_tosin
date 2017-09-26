import random

def checkGuess(guess, actual):
	if guess == actual:
		print("Correct!")
		return True
wordList = {
	'information' : 'It is the processed result of data' , 
	"population" : "The amount of people living in a place",
	"message" : "Giving out information" ,
	"random" : "No particular order",
        "select": "take from a group",
        "abbrivation": "short form for words",
        "approach" : "move towards something or someone",
        "contract" : "a binding agreement that is enforceable by law",
        "create" : "bring into existence",
        "derived" : "formed or developed from something else; not original",
        "labour" : "productive work (especially physical work done for wages)"
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
		print("sorry wrong.please Guess Again")
		anotherChance = input('Try a correct answer this time: ')
		if(checkGuess(anotherChance, randomWord) == True):
			break
