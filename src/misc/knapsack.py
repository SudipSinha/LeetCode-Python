def zero_one_knapsack(
    values: list[float], weights: list[float], weight__max: float
) -> set[int]:
    """Dynamic programming solution.
    Time complexity: O(nw), space complexity: O(nw).
    Recurrence relation: v(n, w) = max{v(n - 1, w), v(n - 1, w - w_k) + v_k}.
    """
    assert len(values) == len(weights)
    n = len(values)
    memo: dict[tuple[float, float], float] = {}
    items_chosen: set[int] = set()

    #   Calculating the maximum possible value.
    def _value_max(items: int = n, reduced_weight_limit: float = weight__max) -> float:
        nonlocal values
        nonlocal weights
        nonlocal memo
        if (items, reduced_weight_limit) in memo:
            return memo[(items, reduced_weight_limit)]
        if items == 0 or reduced_weight_limit <= 0:
            memo[(items, reduced_weight_limit)] = 0
            return memo[(items, reduced_weight_limit)]
        if reduced_weight_limit < weights[items - 1]:
            memo[(items, reduced_weight_limit)] = _value_max(
                items - 1, reduced_weight_limit
            )
            return memo[(items, reduced_weight_limit)]
        memo[(items, reduced_weight_limit)] = max(
            values[items - 1]
            + _value_max(items - 1, reduced_weight_limit - weights[items - 1]),
            _value_max(items - 1, reduced_weight_limit),
        )
        return memo[(items, reduced_weight_limit)]

    _value_max()

    #   Backtracking.
    reduced_weight = weight__max
    for item in range(n, 0, -1):
        if (item - 1, reduced_weight) not in memo or (
            (item - 1, reduced_weight) in memo
            and memo[(item, reduced_weight)] != memo[(item - 1, reduced_weight)]
        ):
            items_chosen.add(item)
            reduced_weight -= weights[item - 1]

    return items_chosen


print(
    zero_one_knapsack(
        values=[7, 9, 5, 12, 14, 6, 12], weights=[3, 4, 2, 6, 7, 3, 5], weight__max=15
    )
)
