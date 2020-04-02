"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


def p_4():
    num_array = tuple(range(999, 99, -1))
    palindrome_list = []
    for i in num_array:
        for j in num_array:
            if is_palindrome(i*j):
                palindrome_list.append((i, j, i*j))
    return sorted(palindrome_list, key=lambda x: x[2], reverse=True)


print(p_4()[0])
