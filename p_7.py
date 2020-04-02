"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?

Answer: 104743
"""
import math


def get_prime(n):

    prime_array = [2]

    i = 3
    while len(prime_array) < n:
        for j in prime_array:
            if i % j == 0:
                break
            if j > math.sqrt(i):
                prime_array.append(i)
                break
        else:
            prime_array.append(i)
        i += 2

    return prime_array[-1]

n = int(input("N: "))

print(get_prime(n))
