def getHitProbability(R: int, C: int, G: list[list[int]]) -> float:
    return sum(sum(row) for row in G) / (R * C)
