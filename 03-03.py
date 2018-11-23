myFiles = open('scores.txt', 'w')

print('Name ' + myFiles.name)
print('Mode ' + myFiles.mode)

myFiles.write('GBJ: 100\nKHD: 99\nBBB: 89')
