#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20141005b: Homework
h_20141005b.py: String methods
"""


def string_methods_a(s):
    """
    String methods A
    """

    row = "| {s_1:<3d} | {s_2:^6d} | {s_3:>7.3f} |".format
    for i in range(len(s)):
        print(row(s_1=s[i][0], s_2=s[i][1], s_3=s[i][2]))


def main():
    """
    Main function
    """
    s = [
        [7, 1954, 0.435],
        [5, 1959, 0.391],
        [1, 1972, 16.076],
        [3, 1980, 9.014],
        [6, 1991, 6.482],
        [4, 1995, 17.99],
        [2, 2001, 6.687],
    ]
    string_methods_a(s)


if __name__ == "__main__":
    main()
