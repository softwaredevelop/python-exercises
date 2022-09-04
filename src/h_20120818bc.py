#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120818bc: Homework
h_20120818bc.py: List methods
"""


from itertools import count


def list_methods_a(li):
    """
    List methods A
    """
    count = 0
    for i in li:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    return count


def list_methods_b(li):
    """
    List methods B
    """
    li.sort()
    return [e for e in li if e[0] == "x"] + [e for e in li if e[0] != "x"]


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
