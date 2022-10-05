#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120818d: Homework
h_20120818d.py: List comprehensions
"""


def list_comprehensions_a(l):
    """
    List comprehensions A
    """
    return [i.upper() for i in l]


def list_comprehensions_b(l):
    """
    List comprehensions B
    """
    return [i.capitalize() for i in l]


def list_comprehensions_c(l):
    """
    List comprehensions C
    """
    return [i for i in l if i % 2 == 0]


def list_comprehensions_d(l):
    """
    List comprehensions D
    """
    return [int(i) for i in l]


def list_comprehensions_e(s):
    """
    List comprehensions E
    """
    return [int(i) for i in s]


def list_comprehensions_f(s):
    """
    List comprehensions F
    """
    return [len(i) for i in s.split()]


def list_comprehensions_g(s):
    """
    List comprehensions G
    """
    return [i[0] for i in s.split()]


def list_comprehensions_h(s):
    """
    List comprehensions H
    """
    return [(i, len(i)) for i in s.split()]


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
    test(
        list_comprehensions_a(["car", "bus", "metro", "train"]),
        ["CAR", "BUS", "METRO", "TRAIN"],
    )
    test(list_comprehensions_a(["car"]), ["CAR"])
    test(list_comprehensions_a([""]), [""])
    test(list_comprehensions_a([]), [])
    test(
        list_comprehensions_a(["car", "bus", "metro", "train", "car", ""]),
        ["CAR", "BUS", "METRO", "TRAIN", "CAR", ""],
    )

    test(list_comprehensions_b(["car"]), ["Car"])
    test(list_comprehensions_b([""]), [""])
    test(list_comprehensions_b([]), [])
    test(
        list_comprehensions_b(["car", "bus", "metro", "train", "car", ""]),
        ["Car", "Bus", "Metro", "Train", "Car", ""],
    )

    test(
        list_comprehensions_c([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        [2, 4, 6, 8, 10],
    )
    test(list_comprehensions_c([1]), [])
    test(list_comprehensions_c([]), [])
    test(list_comprehensions_c([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])
    test(list_comprehensions_c([1, 3, 5, 7, 9]), [])

    test(list_comprehensions_d(["1", "2", "3", "4", "5"]), [1, 2, 3, 4, 5])
    test(list_comprehensions_d(["1"]), [1])
    test(list_comprehensions_d([]), [])

    test(list_comprehensions_e("12345"), [1, 2, 3, 4, 5])
    test(list_comprehensions_e("1"), [1])
    test(list_comprehensions_e(""), [])

    test(
        list_comprehensions_f("The quick brown fox jumps over the lazy dog"),
        [3, 5, 5, 3, 5, 4, 3, 4, 3],
    )
    test(list_comprehensions_f("The"), [3])
    test(list_comprehensions_f(""), [])
    test(list_comprehensions_f(" "), [])
    test(list_comprehensions_f("  "), [])

    test(
        list_comprehensions_g("The quick brown fox jumps over the lazy dog"),
        ["T", "q", "b", "f", "j", "o", "t", "l", "d"],
    )
    test(list_comprehensions_g("The"), ["T"])
    test(list_comprehensions_g(""), [])
    test(list_comprehensions_g(" "), [])
    test(list_comprehensions_g("  "), [])

    test(
        list_comprehensions_h("The quick brown fox jumps over the lazy dog"),
        [
            ("The", 3),
            ("quick", 5),
            ("brown", 5),
            ("fox", 3),
            ("jumps", 5),
            ("over", 4),
            ("the", 3),
            ("lazy", 4),
            ("dog", 3),
        ],
    )
    test(list_comprehensions_h("The"), [("The", 3)])
    test(list_comprehensions_h(""), [])
    test(list_comprehensions_h(" "), [])
    test(list_comprehensions_h("  "), [])
    test(list_comprehensions_h("The quick"), [("The", 3), ("quick", 5)])


if __name__ == "__main__":
    main()
