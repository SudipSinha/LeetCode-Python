def getWrongAnswers(N: int, C: str) -> str:
    return C.replace("A", "C").replace("B", "A").replace("C", "B")
