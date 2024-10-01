"""Can Place Flowers

Link: https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the `flowerbed` without violating the no-adjacent-flowers rule and `false` otherwise.
"""


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    """Idea: for n consecutive empty slots, maximum flowers that can be planted is floor((n-1)/2).
    Time complexity: O(n), space complexity: O(1).
    """
    if len(flowerbed) == 1:
        return (flowerbed[0] == 0 and n in {0, 1}) or (flowerbed[0] == 1 and n == 0)
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1
    if n <= 0:
        return True
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return n == 0
