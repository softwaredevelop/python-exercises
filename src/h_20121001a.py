#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20121001a: Homework
h_20121001a.py: String methods
"""


def string_methods_a(count):
    """
    String methods A
    """
    if count < 10:
        return f"Number: {count}"
    else:
        return "String: many"


def string_methods_b(s):
    """
    String methods B
    """
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


def string_methods_c(s):
    """
    String methods C
    """
    if len(s) < 1:
        return ""
    else:
        stra = s[0]
        strb = "*"
        strc = s[1:]
        return stra + strc.replace(stra, strb)


def string_methods_d(stra, strb):
    """
    String methods D
    """
    if len(stra) < 1 or len(strb) < 1:
        return ""
    else:
        strc = strb[:2] + stra[2:] + " " + stra[:2] + strb[2:]
        return strc


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
    test(string_methods_a(1), "Number: 1")
    test(string_methods_a(10), "String: many")

    test(string_methods_b("spring"), "spng")
    test(string_methods_b("winter"), "wier")

    test(string_methods_c("babble"), "ba**le")
    test(string_methods_c("sqssed"), "sq**ed")

    test(string_methods_d("mix", "pod"), "pox mid")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
