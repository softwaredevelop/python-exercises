#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120818bca: Homework
h_20120818bca.py: List methods
"""


def list_methods_a(l):
    """
    List methods A
    """
    sum = 0
    for i in l:
        if len(i) >= 2 and i[0] == i[-1]:
            sum += 1
    return sum


def list_methods_b(l):
    """
    List methods B
    """
    l1 = []
    for i in l:
        if i[0] == "x":
            l1.append(i)
    l1.sort()
    l2 = []
    for i in l:
        if i[0] != "x":
            l2.append(i)
    l2.sort()
    return l1 + l2


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
    test(list_methods_a(["aba", "xyz", "aa", "x", "bbb"]), 3)
    test(list_methods_a(["", "x", "xy", "xyx", "xx"]), 2)
    test(list_methods_a(["aaa", "be", "abc", "hello"]), 1)

    test(
        list_methods_b(["bbb", "ccc", "axx", "xzz", "xaa"]),
        ["xaa", "xzz", "axx", "bbb", "ccc"],
    )
    test(
        list_methods_b(["ccc", "bbb", "aaa", "xcc", "xaa"]),
        ["xaa", "xcc", "aaa", "bbb", "ccc"],
    )
    test(
        list_methods_b(["mix", "xyz", "apple", "xanadu", "aardvark"]),
        ["xanadu", "xyz", "aardvark", "apple", "mix"],
    )


if __name__ == "__main__":
    main()
