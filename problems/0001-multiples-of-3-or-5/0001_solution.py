"""
File: solution.py

Description: Solve Problem 1.

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/08/2026
"""


def brute_force(n: int) -> int:
    """
    Brute force solution for finding multiples.

    Args:
        n (int): The value for which we are to find all the multiples.

    Returns:
        (int): The sum of all multiples below `n`.
    """
    vals: list[int] = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            vals.append(i)
    return sum(vals)


def sum_nat_nums(end: int, step: int) -> int:
    """
    Compute the sum of all positive multiples of `step` up to and including `end`.

    Evaluates the arithmetic series given:
        step + 2*step + 3*step + ... + n*step
    where n = end // step.

    Args:
        end (int): Upper bound of the range (inclusive).
        step (int): Step size whose multiples are summed.

    Returns:
        (int): The sum of all multiples of `step` up to `end` (inclusive).
    """
    n: int = end // step
    return step * n * (n + 1) // 2


def closed_form(n: int) -> int:
    """
    An implementation of the closed-form solution to this problem.

    Args:
        n (int): The upper bound whose multiples we are to find.

    Returns:
        (int): The sum of multiples `3` and `5` up to the provided `n`.
    """
    # Subtract out the common multiple of `3` and `5` (`15`)
    return sum_nat_nums(n - 1, 3) + sum_nat_nums(n - 1, 5) - sum_nat_nums(n - 1, 15)


if __name__ == "__main__":
    print(brute_force(1000))
    print(closed_form(1000))
