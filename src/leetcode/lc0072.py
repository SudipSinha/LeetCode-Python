"""Edit Distance

Link: https://leetcode.com/problems/edit-distance/

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
*   Insert a character
*   Delete a character
*   Replace a character
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
                    [cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1]]
                )

    return cache[-1][-1]
