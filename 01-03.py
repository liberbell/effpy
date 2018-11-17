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
