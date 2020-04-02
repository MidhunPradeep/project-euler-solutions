"""
The sum of the squares of the first ten natural numbers is,
1**2+2**2+...+10**2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)**2=552=3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Answer: 25164150
"""


def sum_of_squares(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i**2
    return sum_


def square_of_sum(n):
    return sum(range(1, n+1))**2


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


n = 100
# ~ print(sum_of_squares(n))
# ~ print(square_of_sum(n))
print(difference(n))
print()
