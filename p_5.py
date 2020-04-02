"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232792560
"""

from math import sqrt


def get_prime_array(n):

    A = [False, False] + [True for _ in range(2, n + 1)]

    i = 2
    while i <= sqrt(n):
        if A[i]:
            j = i**2
            while j <= n:
                A[j] = False
                j += i
        i += 1

    return [i for i, is_prime in enumerate(A) if is_prime]


def get_prime_factors(n):
    prime_factors = []
    if n < 100000:
        first_limit = n
    else:
        first_limit = 100000
    for i in get_prime_array(first_limit):
        if n == 1:
            break
        while n % i == 0:
            prime_factors.append(i)
            n = n//i
    if n > 1:
        for i in get_prime_array(n):
            if n == 1:
                break
            if i > 1000:
                while n % i == 0:
                    prime_factors.append(i)
                    n = n//i
    return sorted(prime_factors)


prime_factor_list = []
for i in range(2, 21):
    prime_factor_list.append(get_prime_factors(i))

factor_count = {}
for i in range(2, 21):
    max_i = 0
    for factors in prime_factor_list:
        if factors.count(i) > max_i:
            max_i = factors.count(i)
    factor_count[i] = max_i

product = 1
for factor, power in factor_count.items():
    product = product * (factor**power)
print(product)
