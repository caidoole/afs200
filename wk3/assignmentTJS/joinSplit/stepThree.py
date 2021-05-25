#list(friend_list) one per slot
#enter command several times
#use print() to work through the exercise

csv = 'Eric,John,Michael,Terry,Graham,TerryG,Brian'
friends_list = []

splitString = csv.split(',')

friends_list.append(splitString[0])
print(friends_list[0])

friends_list.append(splitString[1])
print(friends_list[1])

friends_list.append(splitString[2])
print(friends_list[2])

friends_list.append(splitString[3])
print(friends_list[3])

friends_list.append(splitString[4])
print(friends_list[4])

friends_list.append(splitString[5])
print(friends_list[5])

friends_list.append(splitString[6])
print(friends_list[6])

print(friends_list)