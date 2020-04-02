"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""

limit = int(input("Limit: "))

multiples_3 = set()
i = 1
while True:
    product = 3*i
    if product < limit:
        multiples_3.add(product)  # Find all multiples of 3 < limit
        i += 1
    else:
        break

multiples_5 = set()
i = 1
while True:
    product = 5*i
    if product < limit:
        multiples_5.add(product)  # Find all multiples of 3 < limit
        i += 1
    else:
        break

# Merge sets to remove duplicates and find sum
print(sum(multiples_3 | multiples_5))
