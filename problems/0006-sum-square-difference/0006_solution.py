"""
File: 0006_solution.py

Description: Project Euler Problem 6: Sum Square Difference

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/14/2026
"""


def brute_force(n: int) -> int:
    """
    Constructs a brute-force solution by summing all values between 0
    and `n` and squaring it, then computing the sum of squares for `n`.

    Args:
        n (int): The value to which we are to compute to.

    Returns:
        (int): The difference between the total squared and the sum of
        squares for any given value `n`.
    """
    total: int = sum(range(n + 1))
    return total**2 - sum(i * i for i in range(n + 1))


def closed_form(n: int) -> int:
    """
    A closed-form solution for this problem using the arithmetic series
    and sum of squares formula.

    Args:
        n (int): The value to which we are to compute.

    Returns:
        (int): The difference between the total squared and the sum of
        squares for any given value `n`.
    """
    sum_nums: int = n * (n + 1) // 2
    sum_squares: int = n * (n + 1) * (2 * n + 1) // 6
    return sum_nums**2 - sum_squares


if __name__ == "__main__":
    print(brute_force(100))
    print(closed_form(100))
