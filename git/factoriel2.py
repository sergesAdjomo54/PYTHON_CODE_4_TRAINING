from functools import reduce

z = 5
fact = lambda z: reduce(lambda x, y: x * y, range(1, z + 1), 1)
print(fact)