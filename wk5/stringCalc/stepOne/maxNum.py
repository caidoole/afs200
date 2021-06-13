def mMfunction(numberList):
    return 'Max: ' + max(numberList) + ' Min: ' + min(numberList) 
listNumbers = []
for x in range(3):

    userInput = input('What is number ' + str(x+1) + ': ')
    listNumbers.append(userInput)

print(mMfunction(listNumbers))