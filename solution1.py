max_attempts = 5
WORD_LIST = ["name","class","place","team","switch"]
import random

def pick_word(listword):
        word = random.choice(listword)
        print("the word is",word)
        return word
    
def get_guess():
         guess=input("Guess a word : ")
         if not guess=="":  
            return guess
        
         else:
            print("word cannot be empty")
            get_guess()

def evaluate_guess():
    print("running evaluation guess")
    word = pick_word(WORD_LIST)
    guess = get_guess()
    if guess == word:
          return True
    else:
          return False
            
            
def play_game():
    if evaluate_guess() == True:
            print("your guess is correct")
            resp = input("do you want to continue Y/N")
            if resp == "Yes":     
              play_game()
            else:
             print("goodbye")
    else:
        attempts = 4
        print("You have ", attempts , "attempts left")
        play_game()
        
play_game()
