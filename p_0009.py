"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000
"""


def solves_p9(triplet):
    a, b, c = triplet
    return a + b + c == 1000


def generate_triplet(m, n):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return (a, b, c)


solved = False
m = 2
while not solved:
    n = 1
    while n < m:
        triplet = generate_triplet(m, n)
        if solves_p9(triplet):
            print(f"{triplet}:")
            a, b, c = triplet
            print(f"{a}+{b}+{c} = {a+b+c}")
            print(f"{a}*{b}*{c} = {a*b*c}")
            solved = True
        n += 1
    m += 1
