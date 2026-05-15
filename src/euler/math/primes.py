"""
File: src/euler/math/primes.py

Description: Contains commonly used functions pertaining to prime numbers.

Author: Spencer Veatch (sveatch@georgefox.edu)

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
        `p_n <= n (log n + log log n) for sufficiently large n`
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


def is_prime(n: int) -> bool:
    """
    Return `True` if `n` is prime using trial divison.

    Checks divisibility up to `sqrt(n)` and skips even
    numbers after 2.

    Args:
        n (int): An integer to test for primality.

    Returns:
        (bool): `True` if `n` is prime, `False` otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit: int = math.isqrt(n)
    return all(n % i != 0 for i in range(3, limit + 1, 2))


def prime_factors(n: int) -> list[tuple[int, int]]:
    """
    Return the prime factorization of `n` as (`prime`, `exponent`) pairs
    using trial division.

    Args:
        n (int): Integer to factor (must be >= 2).

    Returns:
        (list[tuple[int, int]]): A list of (prime, exponent) pairs.

    Raises:
        ValueError: If the provided integer is less then 2.
    """
    if n < 2:
        raise ValueError("n must be >= 2, got: %s", n)

    factors: list[tuple[int, int]] = []

    # Even factors
    count: int = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factors.append((2, count))

    # Odd factors
    factor: int = 3
    limit: int = math.isqrt(n)
    while factor <= limit and n > 1:
        count = 0
        while n % factor == 0:
            n //= factor
            count += 1
        if count > 0:
            factors.append((factor, count))
            limit = math.isqrt(n)
        factor += 2  # skip even candidates

    # Remaining Prime
    if n > 1:
        factors.append((n, 1))
    return factors


def largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of an integer.

    Args:
        n (int): The integer to find the largest prime
        factor of.

    Returns:
        (int): The largest prime factor of `n`
    """
    return max(p for p, _ in prime_factors(n))


def num_prime_divisors(n: int) -> int:
    """
    Return the number of prime divisors of `n`.

    Args:
        n (int): The integer whose prime divisors we are to find.

    Returns:
        (int): The number of prime divisors of `n`.
    """
    result: int = 1
    for _, exp in prime_factors(n):
        result *= exp + 1
    return result
