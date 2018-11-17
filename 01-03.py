firstname = 'Taylor'
lastname = 'Swift'

print(len(firstname))
print(len(lastname))

firstname.__len__()

ages = [0, 11, 43, 12, 10]
print(len(ages))
i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(['bob', 'mary', 'sam']))

candycollection = {'bob' : 10, 'mary' : 7, 'sam' : 18}
print(len(candycollection))
