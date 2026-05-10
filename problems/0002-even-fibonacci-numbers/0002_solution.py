"""
File: solutions.py

Description: Solve Problem 2: Even Fibonacci Numbers

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/09/2026
"""

from collections.abc import Generator


def fibs() -> Generator[int, None, None]:
    """
    Generates an infinite sequence of Fibonacci numbers.

    Generated sequence begins: 1, 2, 3, 5, 8 ...

    Yields:
        (int): The next Fibonacci number in the series.
    """
    a: int = 0
    b: int = 1
    while True:
        yield a + b
        z: int = b  # Placeholder value
        b = a + b
        a = z


def brute_force() -> int:
    """
    Compute the sum of even Fibonacci numbers below four million.

    Iterates through Fibonacci sequence and accumulates even-valued
    terms.

    Returns:
        (int): The sum of all even Fibonacci numbers below four million.
    """
    gen: Generator[int, None, None] = fibs()
    total: int = 0
    for value in gen:
        if value >= 4_000_000:
            break
        if value % 2 == 0:
            total += value
    return total


if __name__ == "__main__":
    print(brute_force())
