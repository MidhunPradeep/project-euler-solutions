from math import sqrt


def get_prime_array(n):
    """
    Return a list of prime numbers using the Sieve of Eratosthenes
    """

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
