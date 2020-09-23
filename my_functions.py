from collections import Counter
from math import sqrt


def get_prime_list(n):
    """
    Return a list of prime numbers using the Sieve of Eratosthenes
    """

    A = [False, False] + [True for _ in range(2, n + 1)]

    i = 2
    while i <= sqrt(n):
        if A[i]:
            j = i ** 2
            while j <= n:
                A[j] = False
                j += i
        i += 1

    return [i for i, is_prime in enumerate(A) if is_prime]


def number_of_factors(n, return_factors=False):
    """
    Return the number of factors of a number.

    Uses the formula:
    Number of factors = (1+a1) * (1+a2) * (1+a3) * … (1+an)
    where a1, a2, a3 …. an are count of distinct prime factors of the number.
    """

    prime_factors = Counter()

    while n % 2 == 0:  # Finds the number of times n can be divided by 2.
        prime_factors[2] += 1
        n //= 2

    i = 3
    while (
        n > 1
    ):  # Finds the number of times n can be divided by every prime odd number > 2.
        while n % i == 0:
            prime_factors[i] += 1
            n //= i
        i += 2

    factor_count = 1
    for count in prime_factors.values():
        factor_count *= count + 1

    if return_factors:
        return factor_count, prime_factors

    return factor_count
