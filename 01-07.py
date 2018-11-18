pointsInGame = [0, -15, 15, -2, 1, 12]

sortedGame = sorted(pointsInGame)
print(sortedGame)

children = ['Sue', 'Jerry', 'Linda']
print(sorted(children))
print(sorted(['Sue', 'jerry', 'linda']))

print(sorted('My favorite child is Lindsa'.split(), key=str.upper))
