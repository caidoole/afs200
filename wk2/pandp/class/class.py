#string.upper()
#userInput = input('What is your input: ')
#print('Your input is: ', userInput.upper())

class upperCase():
    def __init__(self):
        self.userInput = ''

    def getInput(self):
     self.userInput = input('What is your user input: ')

    def displayUpper(self):
        print(self.userInput.upper())

c = upperCase()
c.getInput()
c.displayUpper()