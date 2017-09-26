max_attempts =5
WORD_LIST = ["name","class","place","team","switch"]
import random

def pick_word(listword):
        word = random.choice(listword)
        print("the word is",word)
        return word

def get_guess():
         guess=input("Guess a word : ")
         if not guess == "":  
            return guess
         else:
            print("word cannot be empty")
            get_guess()


def evaluate_guess(word,attempts):
    while attempts > 0:
            guess = get_guess()
            if guess != word:
                    attempts -=1
                    print("wrong attempts,you have",attempts,"left")
                    evaluate_guess(word,attempts)
            else:
                   print("your guess is correct")
                   return True
            break    



    else:
        print("you have used all ure attempts")
        return False


def play_game(game_count):
        game_count += 1
        word = pick_word(WORD_LIST)
        print("welcome to word guess game")
        print()

        while evaluate_guess(word,5):
            ask =input("do you want to continue..? Y/N")
            if ask == "yes":
              play_game(game_count)
            else:
                print("you played",game_count,"games")
                print("goodbye")
                exit()
        else:
                print("opps you missed that one")
                retry = input("do you want to try another word")
                if retry == "yes":
                     play_game(game_count)
                else:
                     print("goodbye")
                     
play_game(0)   
