myFiles = open('scores.txt', 'w')

print('Name ' + myFiles.name)
print('Mode ' + myFiles.mode)

myFiles.write('GBJ: 100\nKHD: 99\nBBB: 89')
myFiles.close()

myFile2 = open('scores.txt', 'r')
print('Reading...' + myFile2.read())
myFile2.close()
