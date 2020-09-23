"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/problem=15

How many such routes are there through a 20×20 grid?

Answer: 137846528820
"""
import functools


@functools.lru_cache
def get_route_count(grid_size, x=0, y=0):

    if x == grid_size and y == grid_size:
        return 1

    possible_routes = 0

    if x < grid_size:
        possible_routes += get_route_count(grid_size, x + 1, y)
    if y < grid_size:
        possible_routes += get_route_count(grid_size, x, y + 1)

    return possible_routes


def main():
    print(get_route_count(20))


main()
