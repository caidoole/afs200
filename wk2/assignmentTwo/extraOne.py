number = int(input('Tell me what is your number: '))

n4 = number % 4 == 0

if n4 == True:
    print('Number is a multiple of 4')
else:
    print('Number is not a multiple of 4 please try again: ')