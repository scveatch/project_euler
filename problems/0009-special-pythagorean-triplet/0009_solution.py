"""
File: 0009_solution.py

Description: Project Euler Problem 9: Special Pythagorean Triplet

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: YYYY-MM-DD
"""


def get_triplet() -> int:
    """
    Get the specified Pythagorean Triplet. Explanation attached in
    LaTeX.

    Returns:
        (int): The product of the natural numbers which compose the
        Pythagorean Triplet.

    Raises:
        ValueError: If no Triplet can be found.
    """
    for i in range(333, 1, -1):
        a: int = i
        b: int = round((500_000 - (1_000 * a)) / (1_000 - a))
        c: int = 1000 - a - b
        if a**2 + b**2 == c**2:
            return a * b * c
    raise ValueError("Triple not found")


def main() -> None:
    """Prints the output of `get_triplet()`"""
    print(get_triplet())


if __name__ == "__main__":
    main()
