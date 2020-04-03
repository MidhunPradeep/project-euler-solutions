"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
"""

import my_functions

n = int(input("N: "))
if n <= 1:
    raise ValueError("n cannot be less than 2.")

print(sum(my_functions.get_prime_list(n)))
