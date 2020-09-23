"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232792560
"""
import my_functions


def get_prime_factors(n):
    prime_factors = []
    if n < 100000:
        first_limit = n
    else:
        first_limit = 100000
    for i in my_functions.get_prime_list(first_limit):
        if n == 1:
            break
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 1:
        for i in my_functions.get_prime_list(n):
            if n == 1:
                break
            if i > 1000:
                while n % i == 0:
                    prime_factors.append(i)
                    n = n // i
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
    product = product * (factor ** power)
print(product)

# This one's a mess right now.
# TODO: Clean up the code and make it accept input.
