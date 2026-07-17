"""Edit Distance

Link: https://leetcode.com/problems/edit-distance/

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
*   Insert a character
*   Delete a character
*   Replace a character

Solution idea:
*   Suppose we want to transform `s` to `t`, and (i, j) is the current position of `s` and `t` respectively. We denote f(i, j) as the minimum number of operations required to transform `s[0:i]` to `t[0:j]`.
*   We have the following cases:
    *   If `s[i] == t[j]`, then we can ignore the last character of both strings and move to the next character. So, f(i, j) = f(i-1, j-1).
    *   If `s[i] != t[j]`, we have three options:
        1.  Insert `t[j]` into `s`, which means we need to transform `s[0:i]` to `t[0:j-1]`. So, f(i, j) = f(i, j-1) + 1.
        2.  Delete `s[i]`, which means we need to transform `s[0:i-1]` to `t[0:j]`. So, f(i, j) = f(i - 1, j) + 1.
        3.  Replace `s[i]` with `t[j]`, which means we need to transform `s[0:i-1]` to `t[0:j-1]`. So, f(i, j) = f(i-1, j-1) + 1.
        The final result is the minimum of the three cases above.
*   We can use dynamic programming + memoization to store the results of the subproblems to avoid redundant calculations. We can create a 2D array `dp` where `dp[i][j]` represents the minimum number of operations required to transform `s[0:i]` to `t[0:j]`. The base case is when one of the strings is empty, in which case we need to insert all characters of the other string. The final result is stored in `dp[len(s)][len(t)]`.
*   The time complexity is `O(mn)` and the space complexity is `O(mn)`, where `m` and `n` are the lengths of the two strings.
"""


def minDistance_recur(word1: str, word2: str) -> int:
    distance__maxplus = max(len(word1), len(word2)) + 1
    cache = [[distance__maxplus] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    #   Base cases.
    for i in range(1 + len(word1)):
        cache[i][0] = i
    for j in range(1 + len(word2)):
        cache[0][j] = j

    def _aux(i: int = len(word1), j: int = len(word2)) -> int:
        """One-based indexing. We look at [0: index]."""
        nonlocal cache

        if cache[i][j] != distance__maxplus:
            return cache[i][j]

        if word1[i - 1] == word2[j - 1]:
            cache[i][j] = _aux(i=i - 1, j=j - 1)
            return cache[i][j]
        cache[i][j - 1] = _aux(i=i, j=j - 1)  # Insert.
        cache[i - 1][j] = _aux(i=i - 1, j=j)  # Delete.
        cache[i - 1][j - 1] = _aux(i=i - 1, j=j - 1)  # Replace.
        cache[i][j] = 1 + min([cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1]])
        return cache[i][j]

    return _aux()


def minDistance_iter(word1: str, word2: str) -> int:
    distance__maxplus = max(len(word1), len(word2)) + 1
    cache = [[distance__maxplus] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    #   Base cases.
    for i in range(1 + len(word1)):
        cache[i][0] = i
    for j in range(1 + len(word2)):
        cache[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = 1 + min(
                    [cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1]],
                )

    return cache[-1][-1]
