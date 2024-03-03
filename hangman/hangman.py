from wordsList import words
from random import randint
from tutorial import tutorial

chosenWord = words[randint(0,99)]
chosenWord = chosenWord.lower()

# tutorial()

def game(word):

    hiddenWord = []
    for i in range(0, len(word)):
        hiddenWord.append('_')

    while ('_' in hiddenWord):
        print(''.join(hiddenWord) + '\n')
        
        letter = input('Guess a letter!\n\n')

        for i in range(0, len(word)):
            if letter == word[i]:
                hiddenWord[i] = word[i]
        
    print('\nGGEZ!!')
        
game(chosenWord)

