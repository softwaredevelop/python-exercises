#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120815d: Homework
h_20120815d.py: List methods
"""


def string_methods_a():
    """
    String methods A
    """
    l = []
    for i in range(33, 127):
        l.append(str(i) + ": " + chr(i))
    return l


def main():
    """
    Main function
    """
    for i in string_methods_a():
        print(i)


if __name__ == "__main__":
    main()
