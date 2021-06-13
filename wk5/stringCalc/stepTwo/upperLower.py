def countTest():
    count = {'UPPER_CASE': 0, 'LOWER_CASE': 0}
    L = input('What would you like to say?: ')

    for u in L:
        if u.isupper():
            count['UPPER_CASE'] +=1
        elif u.islower():
            count['LOWER_CASE']+=1
        else:
            pass
    print('Number of Upper Case Letters: ', count['UPPER_CASE'])
    print('Number of Lower Case Letters: ', count['LOWER_CASE'])

countTest()