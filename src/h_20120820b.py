#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120820b: Homework
h_20120820b.py: Numerical methods
"""


def numerical_methods_a(n):
    """
    Numerical methods A
    """
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * numerical_methods_a(n // 2)


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
    test(numerical_methods_a(156), 10011100)
    test(numerical_methods_a(0), 0)
    test(numerical_methods_a(1), 1)
    test(numerical_methods_a(8432774), 100000001010110010000110)

    test(numerical_methods_a(3), 1)


if __name__ == "__main__":
    main()
