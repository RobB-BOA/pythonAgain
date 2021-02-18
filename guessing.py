import random

def guessGame():

    print('Oh hi, what\'s your name?')

    userName = input()

    print('Hello there ' + userName + '. I am thinking of a number between 1 and 20.')

    secretNo = random.randint(1,20)

    for guesses in range(1,7):
        print('take a guess')
        guess = input()
        if int(guess) < secretNo:
            print('I\'m thinking of a higher number...')
        elif int(guess) > secretNo:
            print('Nah that\'s too high')
        else:
            break
        
    print(guess + ' was it! You did it in ' + str(guesses) + ' guesses!') if int(guess) == secretNo else print('You are terrible at guessing! The number was ' + str(secretNo) + '!')


              
