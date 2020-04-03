"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although
it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Answer: 837799
"""

collatz_chain_dict = {}


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def collatz_chain_length(n):
    original_n = n
    length = 0
    if n == 1:
        return 1
    while n > 1:
        if n in collatz_chain_dict:
            length += collatz_chain_dict[n]
            break
        n = collatz(n)
        length += 1
    collatz_chain_dict[original_n] = length
    return length + 1


limit = int(input("Limit: "))

largest_chain_length = (1, 1)
for i in range(1, limit):
    length = collatz_chain_length(i)
    if length > largest_chain_length[1]:
        largest_chain_length = (i, length)

n, i = largest_chain_length
print(f"Then number {n} has the largest Collatz chain with a length of {i}.")
