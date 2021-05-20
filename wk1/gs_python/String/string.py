name = input('What is your name child? ')
age = int(input('What is your age? '))

#my code - accounting for the year you are 0:
tillHundred = 100 - age
currentYear = 2021 
yearofHundred = currentYear + tillHundred -1
print(name, 'you will turn a 100 in the year', yearofHundred)


#base off your code example in live meeting:
born = 2021 - age
hundred = born + 100 
print(name, 'you will turn 100 in the year', hundred)

#most accurate reflection of how long till 100 would need more information on
#if your birthday has passed or not. both of these lack accuracy for some years (example 40 and 21)