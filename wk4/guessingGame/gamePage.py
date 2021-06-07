import random
goalNum = str(random.randint(1, 100))
print(goalNum) #this is only in for verifying that it is functioning correctly.

welcome = 'Welcome to thy game of guess, my name is Charles I will be your guide.'
print(welcome)

userName = input('Please tell me your name: ')
print('It is a pleasure to meet you, ' + userName)
print ('*****************************************************************')

charles = 'The goal is simple, below is a Die numbered 1 to 100. Guess correct and free yourself. Else the While loops will get you...'
print(charles)
print ('*****************************************************************')

playGame = True 
startGame = input('Do you want to play?: (Yes/Exit): ' )
if startGame.lower() == 'yes':
    print('Lets begin')
else:
    playGame = False
    print('Goodbye')
 
guessCount = 0
while playGame == True:
    userGuess = str(input('What number do you guess?: '))
    print('You have guessed ' + userGuess)
    guessCount +=1

    if userGuess == goalNum:
        playGame = False
        print('Congradualtions!! ' + userName +' You have guessed correctly')
        print('It took you: ' + str(guessCount) + ' attempts')
        print ('*****************************************************************')
        userContinue = input('Would you like to play again? (Yes/Exit): ')
        if userContinue.lower() == 'yes':
            playGame = True
            goalNum = str(random.randint(1, 100))
            guessCount = 0
            print(goalNum)
            print('New number is set! ')
            print ('*****************************************************************')

        else:
            playGame = False 
            print('So long ' + userName + ' happy to have meet you')
            print ('*****************************************************************')

    elif int(userGuess) > int(goalNum) and int(userGuess) <= 100:
        print('Your guess is too High bring it down a bit')
        print ('*****************************************************************')
    elif int(userGuess) < int(goalNum) and int(userGuess) >= 1:
        print('Your guess is to Low, bring it on!')
        print ('*****************************************************************')
    else:
        print('Looks like you are out of bounds, please try again between 1 and 100')
        print ('*****************************************************************')