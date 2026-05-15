"""
File: 0005_solution.py

Description: Project Euler Problem 5: Smallest Multiple

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/09/2026
"""

import functools
import math


def least_common_mult(first: int, second: int) -> int:
    """
    Constructs the least common multiple of two values `first` and `second`.

    Args:
        first (int): The first integer to be evaluated.
        second (int): The second integer to be evaluated.

    Returns:
        (int): The least common multiple of the two provided values.
    """
    return abs(first * second) // math.gcd(first, second)


def smallest_multiple(limit: int) -> int:
    """
    Gets the smallest multiple up to the provided `limit` (inclusive).

    Args:
        limit (int): The value at which to stop evaluation.

    Returns:
        (int): The smallest multiple of all values up to and including `limit`.
    """
    return functools.reduce(least_common_mult, range(1, limit + 1))


if __name__ == "__main__":
    print(smallest_multiple(20))
