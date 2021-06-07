import random

class guessingGame():
    def __init__(self):
        self.goalNum = str(random.randint(1, 100))
        self.userName = ''
        self.play = True
        self.guessCount = 0 
        self.userGuess = ''

    def getUserInput(self, inputType):
        print('Welcome')
        if inputType == 'Name':
            self.userName = input('What is your name? ')
            print('It is a pleasure to meet you, ' + self.userName)
            print ('*****************************************************************')
            print( 'The goal is simple, below is a Die numbered 1 to 100. Guess correct and free yourself. Else the While loops will get you...')
            print ('*****************************************************************')
    def gameStart(self, type):
        if type == 'Start':
            startGame = input('Do you wanna play? (Yes/Exit): ')
            if startGame.lower() == 'yes':
                print('Lets begin')
                self.play = True
                self.playGame()
            else:
                print('Goodbye')
                self.play = False
        elif type == 'Continue':
            contGame = input('Would you like to play again? (Yes/Exit): ')
            if contGame.lower() == 'yes':
                self.play = True
                self.goalNum = str(random.randint(1, 100))
                self.guessCount = 0
                print('New number is ready')
                print ('*****************************************************************')
            else:
                self.play = False 
                print('See ya!')
                print ('*****************************************************************')
    def playGame(self):
        while self.play == True:
            self.userGuess = str(input('What is your number?: '))
            print('You have guessed ' + self.userGuess )
            self.guessCount +=1

            if self.userGuess == self.goalNum:
                print('Congradualtions!! ' + self.userName +' You have guessed correctly')
                print('It took you: ' + str(self.guessCount) + ' attempts')
                print ('*****************************************************************')    
                self.gameStart('Continue')
            
            elif int(self.userGuess) > int(self.goalNum) and int(self.userGuess) <= 100:
                print('Your guess is too High bring it down a bit')
                print ('*****************************************************************')
            elif int(self.userGuess) < int(self.goalNum) and int(self.userGuess) >= 1:
                print('Your guess is to Low, bring it on!')
                print ('*****************************************************************')
            else:
                print('Looks like you are out of bounds, please try again between 1 and 100')
                print ('*****************************************************************')

test = guessingGame()
test.getUserInput('Name')
test.gameStart('Start')