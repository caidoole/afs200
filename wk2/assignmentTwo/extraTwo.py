num = int(input('Pick a number: '))

check = int(input('Pick a check number: '))

answer = num % check

if answer == 0:
    print('Your numbers do divide evenly we are all doomed!')
else:
    print('Your number choices do not divide evenly the wolrd is saved!')