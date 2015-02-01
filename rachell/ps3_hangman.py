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
    while True:
        for x in secretWord: 
            if x  in lettersGuessed:
                continue    
            else:
                return False
                break
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedword = []
    finalguess = 0
    while True:
        for x in secretWord: 
            if x  in lettersGuessed:
                guessedword.append(x)
            if x not in lettersGuessed: 
                
                guessedword.append("_ ")
                            
        break
    finalguess = "".join(guessedword)
    
    return finalguess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = []
    for x in string.ascii_lowercase:
        if x in lettersGuessed:
            continue
        if x not in lettersGuessed:
            availableLetters.append(x)
        notGuessed = "".join(availableLetters)
        
    return notGuessed

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
    print ("Welcome to the game hangman!")
    print ("I am thinkinng of a word that is " + str(len(secretWord)) + " letters long.")
    print ("------------------")

    guessesLeft = 8
    lettersGuessed = []
    b = ''

    while guessesLeft > 0: 
        print ("You have " + str(guessesLeft) + ' guesses left.')
        print ("Available letters: " + str(getAvailableLetters(lettersGuessed)))
        a = raw_input("Please guess a letter: ")

        if a.lower() in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
       
        else:
            lettersGuessed += a.lower()

            if a.lower() in secretWord:
                print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
                b = b + a
            else:

                print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                guessesLeft -= 1

        print("------------")


        if isWordGuessed(secretWord, lettersGuessed) == True :
            print("Congratulations, you won!")
            break

        if guessesLeft == 0 : 
            print ("Sorry, you lost! Try again. The word was ") + str(secretWord)





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
