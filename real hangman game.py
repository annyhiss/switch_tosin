#pick random word
import random
WORDLIST = ("phone", "laptop", "desktop", "sewer", "television", "never", "guess", "nice", "chair", "car");
Word = random.choice(WORDLIST);
Acceptable = ("abcdefghijklmnopqrstuvwxyz");
guessed = [];
gamesWon = 0;
playedOnce = 0;
turns = 10;


#length of word
results = []
for x in s.split():
    word_length = len(x)
    results.append(word_length)
print results 


#definition of word
wordList = {
	'phone' : "modern means of communication" , 
	"laptop" : "modified computer",
	"desktop" : "the visual part of a computer" ,
	"machine" : "equipment used to reduce man labour" ,
        "television" : "a visual means of ommunication" ,
        "never" : "not accepting" ,
        "guess" : "coose without having an idea" ,
        "nice" : "been good" ,
        "labour" : "use of man power" ,
        "car" : "means of transportation" 
}
randomWord, definition = random.choice(list(wordList.items()))
