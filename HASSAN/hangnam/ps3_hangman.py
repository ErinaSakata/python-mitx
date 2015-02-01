# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = False
    for letter in secretWord:
        if letter in lettersGuessed:
            result = True
        else:
            result = False
    return result




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    print result
    count = 0
    for secret in secretWord:
        if secret in lettersGuessed:
            result += secret
        else:
            result += '_ '
    return result




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabets = string.ascii_lowercase
    result = ''
    
    for letter in alphabets:
        if not letter in lettersGuessed:
            result += letter
            
 
    return result 
    





def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = list()
    mistakesMade = 0
    repeat = ''
    dash = '-------------'
    guess = 8
    import string
    availableLetters = string.ascii_lowercase
    if guess == 8:
        print "Welcome to the game, Hangman!"
        print  "I am thinking of a word that is ", len(secretWord), "letters long."
        print dash
        print "You have 8 guesses left."
        print "Available letters: abcdefghijklmnopqrstuvwxyz"
    while (not (isWordGuessed(secretWord,lettersGuessed))) or  (not guess == 0):
        inputguess = raw_input("Please guess a letter:")
        guessInLowerCase = inputguess.lower()
        lettersGuessed.append(guessInLowerCase)
        twice = False
        print availableLetters
        if guessInLowerCase in availableLetters:
            twice = False
            #print "repeat : ", repeat
        else:
            twice = True
            #print "repeat : ", repeat
        availableLetters = getAvailableLetters(lettersGuessed)

        if (guessInLowerCase in secretWord) and (not twice):
            print " secretWord = ", secretWord , " lettersGuessed = ", lettersGuessed
            isGuessed = isWordGuessed(secretWord,lettersGuessed)
            print "isGuessed = ", isGuessed
            if isGuessed:
                print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
                print dash
                print "Congratulations, you won!"
                break
            else:
                print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
                print dash
                print "You have ", guess , " guesses left."
                availableLetters = getAvailableLetters(lettersGuessed)
                print "Available letters: ", availableLetters
        elif twice:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
            print dash
            print "You have ", guess, " guesses left."
            availableLetters = getAvailableLetters(lettersGuessed)
            print "Available letters: ", availableLetters
        else :
            print "Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed)
            outputGraphics(guess)
            guess -= 1
            #print guess

            if not (guess == 0):
                print dash
                print "You have ", guess, " guesses left."
                availableLetters = getAvailableLetters(lettersGuessed)
                print "Available letters: ", availableLetters
            else:
                print dash
                print "Sorry, you ran out of guesses. The word was ", secretWord, "."
                break

        #if (guess == 0):
        #    print dash
        #    print "Sorry, you ran out of guesses. The word was ", secretWord, "."













# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)



def outputGraphics(numGuessesLeft):
    if numGuessesLeft == 7:
        print('|---------|                 |------------------|')
        print('|                           |You got 7 guesses!|')
        print('|                           |Save me pal!      |')
        print('|                           |------------------|')
        print('|                           /')
        print('|                          O')
        print('|  ______                 /|\\')
        print('| |      |                 |')
        print('|_|______|________________/_\\')
    elif numGuessesLeft == 6:
        print('|---------|               |-----------------------|')
        print('|                         |You got 6 guesses!     |')
        print("|                         |C'mon you can save me! |")
        print('|                         |-----------------------|')
        print('|                         /')
        print('|                        O')
        print('|  ______               /|\\')
        print('| |      |               |')
        print('|_|______|______________/_\\__')
    elif numGuessesLeft == 5:
        print('|---------|           |------------------|')
        print('|                     |You got 5 guesses!|')
        print("|                     |it's close to me! |")
        print('|                     |------------------|')
        print('|                     /')
        print('|                    O')
        print('|  ______           /|\\')
        print('| |      |           |')
        print('|_|______|__________/_\\________')
    elif numGuessesLeft == 4:
        print('|---------|         |------------------------------|')
        print('|                   |You got 4 guesses!            |')
        print('|                   |are you sure you can save me! |')
        print('|                   |------------------------------|')
        print('|                   /')
        print('|                  O')
        print('|  ______         /|\\')
        print('| |      |         |')
        print('|_|______|________/_\\__________')
    elif numGuessesLeft == 3:
        print('|---------|        |------------------|')
        print('|                  |You got 3 guesses!|')
        print("|                  |This isn't funny! |")
        print('|                  |------------------|')
        print('|                  /')
        print('|                 O')
        print('|  ______        /|\\')
        print('| |      |        |')
        print('|_|______|_______/_\\___________')
    elif numGuessesLeft == 2:
        print('|---------|      |------------------|')
        print('|                |You got 2 guesses!|')
        print("|                |I don't wanna die!|")
        print('|                |------------------|')
        print('|               /')
        print('|              O')
        print('|  ______     /|\\')
        print('| |      |     |')
        print('|_|______|____/_\\______________')
    elif numGuessesLeft == 1:
        print('|---------|')
        print('|    |      |-----------------------|')
        print("|    |      |You've your last guess!|")
        print('|    O -----|hasta la vista baby!   |')
        print('|   /|\\     |-----------------------|')
        print('|    |')
        print('|  _/_\\__')
        print('| |      |     ')
        print('|_|______|______________________')
    elif numGuessesLeft == 0:
        print('|---------|')
        print('|    |   ')
        print('|    |            Your hero died. Game over!')
        print('|    O')
        print('|   /|\\')
        print('|    |')
        print('|   / \\')
        print('| |\\   /|     ')
        print('|_|_\\_/_|______________________')

secretWord = chooseWord(wordlist).lower()
hangman('abc')
