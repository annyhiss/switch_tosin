WORD_LIST = ["name","class","place","team","switch"]
import random

def pick_word(listword):
        return random.choice(listword)
 def get guess():
        guess=input("Guess a word : ")
 		if not guess=="":
 			return guess
 		else:
 		     print"word cannot be empty"
 		     get_guess()
 def evaluate guess():
 		word=pick_word(WORD_LIST)
 		guess=get-guess()
 		if guess==word:
 	        print("true")
 			return True
 		else:
 			 print("flase")
 			return False
		 evaluate_guess():

 			
 	def play_game():
 		 if evaluate_guess==True:
 		 	print("your guess is correct")
 		 	resp= input("do you want to continue Y/N")
 		 	if resp == "Y":
 		 		evaluate_guess()
 		 	else:
 		 		print("goodbye")