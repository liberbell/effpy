import statistics
import math

ageData = [ 10, 13 ,14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(ageData))
print(statistics.mode(ageData))
print(statistics.median(ageData))
print(sorted(ageData))

print(statistics.variance(ageData))
print(statistics.stdev(ageData))

print(math.sqrt(statistics.variance(ageData)))
