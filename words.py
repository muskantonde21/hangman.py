# import re
# import string 
# import random

# def loadWords():
#     wordlist='/home/muskan/Desktop/hangman/words.txt'
#     inFile = open(wordlist, 'r')
#     line = inFile.readline()
#     wordlist =line.split()
#     # print ("  ", len(wordlist), "words loaded.\n")
#     return wordlist

# def choose_word():
#     """
#     wordlist (list): list of words (strings)
#     ye function ek word randomly return karega
#     """
#     wordlist = loadWords()
#     secretWord = random.choice(wordlist)
#     secretWord = secretWord.lower()

#     return secretWord