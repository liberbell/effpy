import itertools

election = {1: 'Barb', 2: 'Karen', 3: 'Erin'}
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)
