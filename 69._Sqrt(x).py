# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

def mySqrt(x: int) -> int | str:
    if x < 0:
        return 'некорректное число'
    if x == 0:
        return 0

    i = 0
    sqr = i * i
    while x >= sqr:
        i += 1
        sqr = i * i
    return i - 1


# test №1
x = 4
print(mySqrt(x))
# test №2
x = 8
print(mySqrt(x))
# test №3
x = -1
print(mySqrt(x))
