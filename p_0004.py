"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""


def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:  # Checks if string(n) is equal to it's reverse
        return True
    return False


def largest_palindrome(start, stop):
    # Example: Convert a range(1, 1000) -> range(999, 0, -1)
    reverse_start = stop - 1
    reverse_stop = start - 1
    num_array = tuple(range(reverse_start, reverse_stop, - 1))

    palindrome_list = []
    for i in num_array:
        for j in num_array:
            product = i * j
            if is_palindrome(product):  # Generate a tuple of i and j if i * j is a palindrom
                palindrome_list.append((i, j, product))

    # Return the tuple with the largest value of i * j
    return sorted(palindrome_list, key=lambda x: x[2], reverse=True)[0]


print("lower_limit <= x < upper_limit\n")
lower_limit = int(input("Lower limit: "))
upper_limit = int(input("Upper limit: "))

palindrome_list = largest_palindrome(lower_limit, upper_limit)
a = palindrome_list[0]
b = palindrome_list[1]
c = palindrome_list[2]

print(f"\nLargest palindrome product: {a} * {b} = {c}")
