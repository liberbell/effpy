isRaining = True
isSunny = False

if isRaining and isSunny:
    print('We might see a rainbow')

if isRaining or isSunny:
    print('It might be rainy or it might be sunny')

if not isRaining:
    print('It must be raining')

ages = [12, 18, 39 ,87, 7, 2]
for age in ages:
    isAdult = age > 17;
    if not isAdult:
        print('Being ' + str(age) + ' does not make you an adult.')
