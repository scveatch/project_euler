"""
File: 0008_solution.py

Description: Project Euler Problem 8: Largest Product in a Series

Author: Spencer Veatch (sveatch@willamette.edu)

Last Modified: 05/16/2026
"""

import math


def sliding_window(arr: list[int], window_size: int) -> int:
    """
    Return the maximum product of a continguous window of a fixed size.
    Iterates through `arr`, computes the product of each continguous subarray
    of length `window_size`, and returns the largest product.

    Args:
        arr (list[int]): A list of integers to search through.
        window_size (int): The number of adjacent elements to include in each
        subarray.

    Returns:
        (int): The maximum product of any continguous subarray of size `window_size`,
        or 0 if no valid window exists.
    """
    if len(arr) < window_size:
        return 0
    max_val: int = math.prod(arr[:window_size])

    for i in range(len(arr) - window_size):
        window_prod: int = math.prod(arr[i : window_size + i])
        max_val = max(max_val, window_prod)

    return max_val


def main() -> None:
    """Loads the provided 1000-digit number and prints the greatest product."""
    with open("number.txt") as f:
        content: str = f.read()
        int_list: list[int] = [int(x) for x in content.strip()]
        x = sliding_window(int_list, 13)
        print(x)


if __name__ == "__main__":
    main()
