"""Number of Provinces

Link: https://leetcode.com/problems/number-of-provinces/

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n × n` matrix isConnected where `isConnected[i][j] = 1` if the `i`th city and the `j`th city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.
"""


def findCircleNum(isConnected: list[list[int]]) -> int:
    if not isConnected:
        return 0
    n = len(isConnected)
    map_node_component = [0] * n
    components__total = 0

    def _dfs(source: int, component__cur: int):
        nonlocal map_node_component
        if map_node_component[source] != 0:
            return
        map_node_component[source] = component__cur
        for dest in range(n):
            if source != dest and isConnected[source][dest] == 1:
                _dfs(source=dest, component__cur=component__cur)

    for i in range(n):
        if map_node_component[i] == 0:
            components__total += 1
            _dfs(source=i, component__cur=components__total)

    return components__total
