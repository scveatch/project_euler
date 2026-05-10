"""
File: solution.py

Description: Solves problem 3

Author: Spencer Veatch (sveatch@wilamette.edu)

Last Modified: 05/09/2026
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


def largest_prime(n: int) -> int:
    """
    Return the largest prime factor of `n`.

    Generates all primes up to sqrt(n) using the Sieve of Eratosthenes,
    the repeatedly divides out prime factors from `n`.

    Args:
        n (int): Positive integer to factor.

    Returns:
        (int): Largest prime factor.
    """
    largest: int = 1

    for p in sieve_eratosthenes(n):
        while n % p == 0:
            largest = p
            n //= p
    return largest


if __name__ == "__main__":
    print(largest_prime(60))
