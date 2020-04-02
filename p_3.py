"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Answer: 6857
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
    prime_factors = set()
    for i in get_prime_array(100000):
        if n == 1:
            break
        while n % i == 0:
            prime_factors.add(i)
            n = n//i
    if n > 1:
        for i in get_prime_array(n):
            if n == 1:
                break
            if i > 1000:
                while n % i == 0:
                    prime_factors.add(i)
                    n = n//i
    return prime_factors


n = int(input("N: "))
a = get_prime_factors(n)
print(a)
print(max(a))
