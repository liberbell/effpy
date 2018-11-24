myFiles = open('scores.txt', 'w')

print('Name ' + myFiles.name)
print('Mode ' + myFiles.mode)

myFiles.write('GBJ : 100\nKHD : 99\nBBB : 89')
myFiles.close()

myFile2 = open('scores.txt', 'r')
print('Reading...\n' + myFile2.read(10))
print('Reading again\n' + myFile2.read())
myFile2.close()
