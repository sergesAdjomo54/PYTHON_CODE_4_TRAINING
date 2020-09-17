import math


def triangle_area(a, b, c):
	p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a
