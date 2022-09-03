#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20120815c: Homework
h_20120815c.py: String methods
"""


def string_methods_e(s):
    """
    String methods E
    """
    if len(s) >= 3:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s


def string_methods_f(s):
    """
    String methods F
    """
    if s.find("not") != -1 and s.find("bad") != -1 and s.find("not") < s.find("bad"):
        return s.replace(s[s.find("not") : s.find("bad") + len("bad")], "good")
    else:
        return s


def string_methods_g(s_1, s_2):
    """
    String methods G
    """

    def front(s):
        """
        Return the first half of the string
        """
        return s[: -(len(s) // 2)]

    def back(s):
        """
        Return the second half of the string
        """
        return s[-(len(s) // 2) :]

    return front(s_1) + front(s_2) + back(s_1) + back(s_2)


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
    test(string_methods_e("string"), "stringly")
    test(string_methods_e("str"), "string")
    test(string_methods_e("st"), "st")

    test(string_methods_f("This dinner is not that bad!"), "This dinner is good!")
    test(string_methods_f("This movie is not so bad!"), "This movie is good!")
    test(string_methods_f("This dinner is bad!"), "This dinner is bad!")

    test(string_methods_g("abcd", "xy"), "abxcdy")
    test(string_methods_g("abcde", "xyz"), "abcxydez")
    test(string_methods_g("abcdef", "xyz"), "abcxydefz")


if __name__ == "__main__":
    main()
