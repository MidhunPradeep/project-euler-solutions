"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
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


n = int(input("N: "))
if n <= 1:
    raise ValueError("n cannot be less than 2.")

print(sum(get_prime_array(n)))
