pointsInGame = [0, -15, 15, -2, 1, 12]

sortedGame = sorted(pointsInGame)
print(sortedGame)

children = ['Sue', 'Jerry', 'Linda']
print(sorted(children))
print(sorted(['Sue', 'jerry', 'linda']))

print(sorted('My favorite child is Lindsa'.split(), key=str.upper))
print(sorted(pointsInGame, reverse=True))

leaderBoard = {231: 'CKL', 123: 'ABC', 432: 'JKC'}
print(sorted(leaderBoard, reverse=True))
