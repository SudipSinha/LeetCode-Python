from collections import deque
from functools import cache
from sys import maxsize


def coinChange_dp(coins: list[int], amount: int) -> int:
    """Recursion relation:
    f(t) = min{1 + f(t - c): c ∈ C, t ≥ c}, min∅ = -1
    f(0) = -1
    Time complexity: O(n), space complexity: O(1).
    """

    @cache
    def _coins__min(target: int = amount) -> int:
        nonlocal coins
        if target == 0:
            return 0

        possibilities = set()
        for coin in coins:
            if coin <= target:
                possibilities.add(1 + _coins__min(target - coin))
        if not possibilities:
            return maxsize
        return min(possibilities)

    coins__min = _coins__min()
    return coins__min if coins__min < maxsize else -1


def coinChange_bfs(coins: list[int], amount: int) -> int:
    """Breadth-first search on tree created by subtracting coins from amount.
    Time complexity: O(n), space complexity: O(n).
    """
    queue: deque[tuple[int, int]] = deque()
    seen: set[int] = set()
    queue.append((amount, 0))
    while queue:
        (target, n_coins) = queue.popleft()
        if target == 0:
            return n_coins
        for coin in coins:
            if coin <= target and (target - coin) not in seen:
                queue.append((target - coin, n_coins + 1))
                seen.add(target - coin)
    return -1
