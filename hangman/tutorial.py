def tutorial():
    tutorial = int(input('''
    Welcome to (really scuffed) Hangman!
    Would you like to learn how to play? 
    (c'mon man if you don't know how then i dunno what to say)

        
    [1] - No thanks nerd
    [2] - Wtf is hangman bruh
                    
    '''))

    if tutorial == 1:
        print('\nReady?\n')
    elif tutorial == 2:
        print('''
        are you serious bro...
        
        Okay, so there's a word you have to guess.
        Only the length of the word is provided.
        You have to reveal the word one letter at a time.
        If the word contains your guessed letter, it will reveal where.
        Otherwise, you lose a life.
        
        Ready?
        ''')

