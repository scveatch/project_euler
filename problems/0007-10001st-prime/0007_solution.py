"""
File: 0007_solution.py

Description: Project Euler Problem 7: 10001st Prime

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/14/2026
"""

import math


def sieve_eratosthenes(limit: int) -> list[int]:
    """
    Return all prime numbers <= to `limit`.

    Iteratively marks composite numbers starting from each discovered prime.

    Args:
        limit (int): Inclusive upper bound for the generated prime numbers.

    Returns:
        (list[int]): A list of all prime numbers <= `limit`.
    """
    is_prime: list[bool] = [True] * (limit + 1)

    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            for mult in range(p * p, limit + 1, p):
                is_prime[mult] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def upper_bound_prime(n: int) -> int:
    """
    Estimates an upper bound estimate for the nth prime.

    Uses the Prime Number Theorem, which estimates that the prime number
    counting theorem `pi(n) ~ x/log(x)`.

    A known asymptotic inversion gives:
        p_n <= n (log n + log log n) for sufficiently large n
    This implementation uses that bound with a safety check for small
    values of `n`.

    Args:
        n (int): Index of the prime (1-indexed). `n = 1` returns an estimate
        for the first prime `2`.

    Returns:
        (int): A value which is guaranteed (for sufficiently large `n`) to be
        >= the nth prime.
    """
    if n <= 6:
        return 15
    return math.ceil(n * (math.log(n) + math.log(math.log(n))))


def solve(n: int) -> int:
    """
    Find upper bound for nth prime, and generate all primes between
    [0, bound]. Index for nth prime.

    Args:
        n (int): The prime number to be returned.

    Returns:
        (int): The `nth` prime.
    """
    max: int = upper_bound_prime(n)
    vals: list[int] = sieve_eratosthenes(max)
    return vals[n - 1]


if __name__ == "__main__":
    print(solve(10_001))
