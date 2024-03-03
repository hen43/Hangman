from wordsList import words
from random import randint
from tutorial import tutorial

chosenWord = words[randint(0,99)]
chosenWord = chosenWord.lower()

# tutorial()

def game(word):
    
    tries = 6

    hiddenWord = []
    for i in range(0, len(word)):
        hiddenWord.append('_')

    while ('_' in hiddenWord and tries > 0):
        print(f'{tries} tries remaining.')
        print(''.join(hiddenWord) + '\n')
        
        found = False
        
        letter = input('Guess a letter!\n\n')
    
        for i in range(0, len(word)):
            if letter == word[i]:
                hiddenWord[i] = word[i]
                found = True
            
        if found == False:
            tries -= 1
        
    if '_' in hiddenWord:
        print('nice try bro')
    else:
        print('LETS GOOOOO!!!! GGEZZZZZZ!!!')
        
game(chosenWord)

