"""Letter Combinations of a Phone Number

Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from `2`-`9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from itertools import product


def letterCombinations(digits: str) -> set[str]:
    map_digit_letters = {
        "2": {"a", "b", "c"},
        "3": {"d", "e", "f"},
        "4": {"g", "h", "i"},
        "5": {"j", "k", "l"},
        "6": {"m", "n", "o"},
        "7": {"p", "q", "r", "s"},
        "8": {"t", "u", "v"},
        "9": {"w", "x", "y", "z"},
    }
    digits_list = list(digits)
    letters_list = (map_digit_letters[digit] for digit in digits_list)
    products = product(*letters_list)
    possibilities = set(map(lambda prod: "".join(prod), products))
    return possibilities if possibilities != {""} else set()
