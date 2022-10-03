#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120818a: Homework
h_20120818a.py: Tuple methods
"""
from math import hypot, sqrt


def tuple_methods_a(t1, t2):
    """
    Tuple methods A
    """
    # return sqrt((t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2)
    return hypot(t2[0] - t1[0], t2[1] - t1[1])


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
    test(tuple_methods_a((0, 0), (0, 0)), 0.0)
    test(tuple_methods_a((0, 0), (0, 1)), 1.0)
    test(tuple_methods_a((0, 0), (1, 0)), 1.0)
    test(tuple_methods_a((0, 0), (1, 1)), sqrt(2))
    test(tuple_methods_a((0, 0), (2, 2)), sqrt(8))
    test(tuple_methods_a((0, 0), (3, 4)), 5.0)


if __name__ == "__main__":
    main()
