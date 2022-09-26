#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120905b: Homework
h_20120905b.py: List methods
"""


def list_methods_a(l):
    """
    List methods A
    """
    sum = 0
    for i in l:
        sum += i
    return sum


def list_methods_b(l):
    """
    List methods B
    """
    mlt = 1
    for i in l:
        mlt *= i
    return mlt


def test(got, expected):
    """
    Test function
    """
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print(f"{prefix} got: {got} expected: {expected}")


def main():
    """
    Main function
    """
    test(list_methods_a([1, 2, 3, 4, 5]), 15)
    test(list_methods_a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
    test(list_methods_a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 120)
    test(list_methods_a([1, 1, 1]), 1)
    test(list_methods_a([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)

    test(list_methods_b([1, 2, 3, 4, 5]), 120)
    test(list_methods_b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3628800)
    test(
        list_methods_b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        1307674368000,
    )
    test(list_methods_b([1, 2, 3, 4, 5]), 1)
    test(list_methods_b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 1)


if __name__ == "__main__":
    main()
