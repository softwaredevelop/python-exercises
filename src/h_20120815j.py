#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120815j: Homework
h_20120815j.py: String methods
"""


def string_methods_a(n):
    """
    String methods A
    """
    if len(str(n)) == 1 or str(n)[-1:] != "0":
        return int(str(n)[::-1])
    else:
        return None


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
    test(string_methods_a(1977), 7791)
    test(string_methods_a(12568), 86521)
    test(string_methods_a(19770), 7791)
    test(string_methods_a(0), 0)
    test(string_methods_a(1), 1)


if __name__ == "__main__":
    main()
