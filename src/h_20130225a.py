#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20130225a: Homework
h_20130225a.py: String methods
"""

import re


def string_methods_a(s):
    """
    String methods A
    """
    return re.sub(r"[\n]*", "", s)


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
    test(string_methods_a("192.20.246.138:\n 6666"), "192.20.246.138: 6666")
    test(string_methods_a("206.130.99.82:\n8080"), "206.130.99.82:8080")


if __name__ == "__main__":
    main()
