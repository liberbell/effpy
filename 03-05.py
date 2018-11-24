myFile = open('scores.txt', 'r')

print('My one line: ' + myFile.readline())
print('My one line: ' + myFile.readline())
myFile.seek(0)

for line in myFile:
    newHighScore = line.replace('BBB', 'PDJ')
    print(line)
    print(newHighScore)

myFile.close()
