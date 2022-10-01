#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120818e: Homework
h_20120818e.py: List methods
"""


def list_methods_a(n):
    """
    List methods A
    """
    l = [i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0]
    return sum(l)


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
    test(list_methods_a(10), 33)
    test(list_methods_a(100), 2418)
    test(list_methods_a(1000), 234168)

    test(list_methods_a(0), 1)
    test(list_methods_a(10), 1)
    test(list_methods_a(100), 1)


if __name__ == "__main__":
    main()
