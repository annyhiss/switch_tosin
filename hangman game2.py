import random
WORDLIST = ("phone", "laptop", "desktop", "sewer", "television", "never", "guess", "nice", "chair", "car");
Word = random.choice(WORDLIST);
Acceptable = ("abcdefghijklmnopqrstuvwxyz");
guessed = [];
state = 0;
gamesWon = 0;
playedOnce = 0;
turns = 10;
def main():
    global guessed, gamesWon, state, playedOnce, turns, WORD, WORDLIST;
    setup_game();
    print ("My word is " , str(WORD) , " letters long.");
    while (wantsToPlay() == 1):
        WORD = random.choice(WORDLIST);
        guessed = [];
        playedOnce = 1;
        gamesWon = 0;
        state = 0;
    while (hasGuessed() == 0 and state < 10):
            drawWord();
            takeNewLetter();
    print("My word was " + WORD);
    
def wantsToPlay():
    if (not playedOnce):
        return 1;
    l = input("\nWould you like to play again? (y/n)");
    while (l != "y" and l != "Y" and l != "n" and l != "N"):
        l = input("\nWould you like to play again? (y/n)");
    if (l.lower() == "y"):
        return 1;
    return 0;
def takeNewLetter():
    global state, gamesWon;
    newPrint("So far, you have guessed the following letters...");
    for g in guessed:
        print(g, end=" ");
    letter = input("\n\nWhat letter would you like to guess next?\n");
    while (letter in guessed or letter not in ACCEPTABLE):
        if (len(letter) > 1):
            if (letter.lower() == WORD.lower()):
                 newPrint("You win!");
                 gamesWon = 1; 
                 break;
            else:
                newPrint("Boo... that was wrong... you're dead...");
                turns = 7;
                break;
        else:
            if (letter not in ACCEPTABLE):
                letter = input("That character is unacceptable. You many only enter lower case letters.\n");
            else:
                letter = input("You have already guessed that letter, try another one...\n");
    guessed.append(letter);
    if (letter not in WORD):
        turns += 1;
    return;
def drawWord():
    tempWord = "";
    for c in WORD:
        if (c in guessed):
            tempWord += c + " ";
        else:
            tempWord += "_ ";
    newPrint(tempWord);
    return;
def hasGuessed():
    if (gamesWon == 1):
        return 1;
    if (turns >= 7):
        return 1;
    for c in WORD:
        if (c not in guessed):
            return 0;
    if (len(guessed) == 0):
        return 0;
    return 1;
 
def setup_game():
    newPrint("Welcome to the Hangman game!");
    newPrint("I have chosen a random word from my super secret list, try to guess it before your stickman dies!");
 
def newPrint(message, both = 1):
    msg = "\n" + message;
    if (both != 1):
        msg += "\n";
    print(msg);
