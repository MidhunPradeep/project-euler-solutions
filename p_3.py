"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Answer: 6857
"""

import my_functions


def get_prime_factors(n):
    prime_factors = set()

    # Divides n by every prime number < 10000 to check if it is a factor until n == 1.
    # This is enough to completely factorise 600851475143 in a small amount of time.
    for i in my_functions.get_prime_array(100000):
        if n == 1:
            break
        while n % i == 0:
            prime_factors.add(i)
            n = n // i

    # If n > 1, do it all over again with a bigger prime number list. Shouldn't activate unless
    # number is ridiculously large.
    if n > 1:
        for i in my_functions.get_prime_array(n):
            if n == 1:
                break
            if i > 10000:
                while n % i == 0:
                    prime_factors.add(i)
                    n = n // i

    # Converts the set into a list and sorts it.
    return sorted(list(prime_factors))


n = int(input("N: "))

a = get_prime_factors(n)
print(f"Factors of {n}: {a}")
print(f"Largest factor: {max(a)}")
