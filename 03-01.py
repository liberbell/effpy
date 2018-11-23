import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Arguments:', sys.argv)

sys.argv.remove(sys.argv[0])
print('Arguments:', sys.argv)

arguments = sys.argv
sum = 0
for arg in arguments:
    print(arg)
