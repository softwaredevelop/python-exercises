#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120815a: Homework
h_20120815a.py: Command line methods
"""


import sys


def cl_methods_a():
    """
    Command line methods A
    """
    if len(sys.argv) == 3:
        return int(sys.argv[1]) + int(sys.argv[2])
    else:
        return "Error: <num_1> <num_2> required"


def main():
    """
    Main function
    """
    print(cl_methods_a())


if __name__ == "__main__":
    main()
