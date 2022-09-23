#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
h_20130218a: Homework
h_20130218a.py: String methods
"""


TEXT_A = """
NULL4M PL4C3R47 L1B3R0 V3L17, 517 4M37 UL7R1C35 PURU5 UL7R1C35 1N. 1N
1N M37U5 4UC70R, F1N1BU5 PURU5 3U, UL7R1C135 M37U5. V3571BULUM
P3LL3N735QU3 N151 1D 50D4L35 14CUL15. P3LL3N735QU3 H4B174N7 M0RB1
7R1571QU3 53N3C7U5 37 N37U5 37 M4L35U4D4 F4M35 4C 7URP15 3G35745.
V1V4MU5 M0L35713 4N73 1N D14M 14CUL15, QU15 D1C7UM NUNC 53MP3R. D0N3C
0RN4R3 357 N3C M1 50D4L35, V1743 M0L35713 D14M PH4R37R4. M0RB1 N3C
DU1 4C 3R47 BL4ND17 P05U3R3. 5U5P3ND1553 P073N71. 43N34N RU7RUM L1B3R0
1N M0LL15 VULPU7473. 43N34N C0NV4LL15 L0R3M N0N M4GN4 53MP3R 1MP3RD137.
"""


def string_methods_a(s):
    """
    String methods A
    """
    # s = s.replace("0", "O")
    # s = s.replace("1", "I")
    # s = s.replace("3", "E")
    # s = s.replace("4", "A")
    # s = s.replace("5", "S")
    # s = s.replace("7", "T")
    dict = {
        "0": "O",
        "1": "I",
        "3": "E",
        "4": "A",
        "5": "S",
        "7": "T",
    }
    for d in dict:
        s = s.replace(str(d), dict[str(d)])
    return s


TEXT_B = """
NULLAM PLACERAT LIBERO VELIT, SIT AMET ULTRICES PURUS ULTRICES IN. IN
IN METUS AUCTOR, FINIBUS PURUS EU, ULTRICIES METUS. VESTIBULUM
PELLENTESQUE NISI ID SODALES IACULIS. PELLENTESQUE HABITANT MORBI
TRISTIQUE SENECTUS ET NETUS ET MALESUADA FAMES AC TURPIS EGESTAS.
VIVAMUS MOLESTIE ANTE IN DIAM IACULIS, QUIS DICTUM NUNC SEMPER. DONEC
ORNARE EST NEC MI SODALES, VITAE MOLESTIE DIAM PHARETRA. MORBI NEC
DUI AC ERAT BLANDIT POSUERE. SUSPENDISSE POTENTI. AENEAN RUTRUM LIBERO
IN MOLLIS VULPUTATE. AENEAN CONVALLIS LOREM NON MAGNA SEMPER IMPERDIET.
"""


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
    test(string_methods_a(TEXT_A), TEXT_B)
    test(string_methods_a(TEXT_B), TEXT_A)


if __name__ == "__main__":
    main()
