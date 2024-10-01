"""Greatest Common Divisor of Strings

Link:

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.
"""

from operator import itemgetter


def divide(dividend: str, divisor: str) -> dict[str, int | str]:
    remainder = ""
    quotient = 0
    while dividend[quotient * len(divisor) : (quotient + 1) * len(divisor)] == divisor:
        quotient += 1
    remainder = dividend[quotient * len(divisor) :]
    return {"quotient": quotient, "remainder": remainder}


def gcdOfStrings(str1: str, str2: str) -> str:
    (dividend, divisor) = (str1, str2) if len(str1) >= len(str2) else (str2, str1)
    (quotient, remainder) = itemgetter("quotient", "remainder")(
        divide(dividend, divisor)
    )
    while quotient != 0 and remainder != "":
        dividend = divisor
        divisor = remainder
        (quotient, remainder) = itemgetter("quotient", "remainder")(
            divide(dividend, divisor)
        )
    return divisor if quotient != 0 else ""
