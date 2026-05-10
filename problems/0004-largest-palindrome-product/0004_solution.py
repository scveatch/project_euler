"""
File: 0004_solution.py

Description: Project Euler Problem 4: Largest Palindrome Product

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/09/2026
"""


def make_palindrome(n: int) -> int:
    """
    Construct a palindrome by mirroring `n`.

    Ex:
        123 -> 123321

    Args:
        n (int): The number to be mirrored.

    Returns:
        (int): `n`, mirrored and in palindrome form.
    """
    s = str(n)
    return int(s + s[::-1])


def factorable(n: int) -> bool:
    """
    Determine if `n` is factorable by 2 3-digit numbers.

    Args:
        n (int): An integer value to be checked.

    Returns:
        (bool): `True` if the value can be factored by 3-digit numbers, `False` otherwise.
    """
    for factor in range(999, 99, -1):
        if factor * factor < n:
            break
        if n % factor == 0:
            other: int = n // factor

            if 100 <= other <= 999:
                return True
    return False


def find_largest() -> int:
    """
    Finds the largest palindrome number made from 2 3-digit numbers.

    Returns:
        (int): The largest palindrome number.
    """
    for val in range(999, 99, -1):
        pal: int = make_palindrome(val)

        if factorable(pal):
            return pal
    raise ValueError("No factorable palindrome numbers found.")


if __name__ == "__main__":
    print(find_largest())
