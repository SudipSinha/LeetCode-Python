"""Keys and Rooms

Link: https://leetcode.com/problems/keys-and-rooms/

There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked except for room `0`. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array `rooms` where `rooms[i]` is the set of keys that you can obtain if you visited room `i`, return `true` if you can visit all the rooms, or `false` otherwise.
"""


def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    """Time complexity: O(n), space complexity: O(n)."""
    visited = [False] * len(rooms)

    def _dfs(room: int):
        nonlocal visited
        if not visited[room]:
            visited[room] = True
            for key in rooms[room]:
                _dfs(key)

    _dfs(room=0)
    return all(visited)
