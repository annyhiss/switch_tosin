max_attempts = 5
def evaluate_guess(attempts_left):
    guess = get_guess()
    word = ""
    if attempts_left == 5:
        word = pick_word(WORD_LIST)
        if guess == word:
            print("your guess is correct")
            retry = input("do you want to retry ? Y/N")
            if retry =="y"
                word = pick_word(WORD_LIST)
                attempts_left -=1
                print("wrong guess")
                guess = get_guess()
                evaluate_guess(attempts_left)

        else:
            attempts_left -=1
            print("wrong guess")
            guess = get_guess()
            evaluate_guess(attempts_left)


def play_game():
    while True:
        game_count +=1
        attempts = 0
        word = pick_word(WORD_LIST)
        guess = get_guess(
        evaluate_guess(guess,word,attempts)
    
