#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120815e: Homework
h_20120815e.py: String methods
"""


def string_methods_a(s):
    """
    String methods A
    """
    return s[::-1]


def string_methods_b(s):
    """
    String methods B
    """
    i = -len(s)
    while i < 0:
        s += s[-i - 1]
        i += 1
    return s[int(len(s) / 2) :]


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
    test(string_methods_a("kayak"), "kayak")
    test(string_methods_a("level"), "level")
    test(string_methods_a(""), "")
    test(string_methods_a("a"), "a")
    test(string_methods_a("hello"), "hello")

    test(string_methods_b("kayak"), "kayak")
    test(string_methods_b("level"), "level")
    test(string_methods_b(""), "")
    test(string_methods_b("a"), "a")
    test(string_methods_b("hello"), "hello")


if __name__ == "__main__":
    main()
