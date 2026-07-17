# you can write to stdout for debugging purposes, e.g.
# print("This is a debug message")

# abb[a]
# [c]abac
# A[bb]--A
# cabc -> c[b]abc

# Either that I insert at the ends:
# Check whether s[1:] or s[:end-1] is palindromic


# is palindrome or not after adding or removing one character.
def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def is_palindome_close(s: str) -> bool:
    n = len(s)
    i = 0
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            break
    non_palindromic = s[i : n - i]
    return is_palindrome(non_palindromic[1:]) or is_palindrome(non_palindromic[:-1])


test_cases = {
    "abcd": False,
    "abb": True,
    "abac": True,
    "xxabacxx": True,
    "yyabcyy": False,
}
for test in test_cases:
    assert is_palindome_close(test) == test_cases[test]


# There are n lists, group them by 'm' number of items.

# E.g. input: lists=[["A1", "A2", "A3", "A4", "A5", "A6"], ["B1", "B2", "B3"], ["C1", "C2", "C3", "C4"]], m=3
# output: [["A1", "A2"], ["B1", "B2"], ["C1", "C2"], ["A3", "A4"], ["B3", "C3"], ["A5", "A6"], ["C4"]]

from collections import deque
from math import ceil

# def reshape(lists: list[list[str]], m: int) -> list[list[str]]:
#     count_total = sum(len(l) for l in lists)
#     result = [[] * ceil(count_total / m)]
#     indices = [0 for l in lists]
#     current_list = 0
#     for r in result:
#         count = 0
#         while count < m:
#             for i in list(current_list, len(lists) - 1) + list(range(0, current_list - 1))
#             for (i, l) in enumerate(lists):
#                 while i < len(l) and count < m:
#                     r.extend(l[indices[i]])
#                     indices[i] += 1
#                     count += 1


def reshape(lists: list[list[str]], m: int) -> list[list[str]]:
    # count_total = sum(len(l) for l in lists)
    # result = [[] * ceil(count_total / m)]
    queue = deque(lists)
    count = 0
    result: list[list[str]] = []
    result.append([])
    while queue:
        current_list = queue.popleft()
        print(f"{current_list=}")
        while count < m:
            if current_list and count < m:
                result[-1].extend(current_list.pop(0))
                count += 1
        if count == m:
            result.append([])
            count = 0
            break
        queue.append(current_list)
    return result


sample = [
    ["A1", "A2", "A3", "A4", "A5", "A6"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3", "C4"],
]
print(reshape(sample, 2))
