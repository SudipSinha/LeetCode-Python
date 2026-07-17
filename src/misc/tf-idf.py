import re
from collections import Counter
from math import log2


def get_tf(term: str, doc: str) -> float:
    term_counter = Counter(re.split(pattern=r"\W", string=doc, flags=re.IGNORECASE))
    return term_counter[term] / sum(term_counter.values())


def get_idf(term: str, corpus: list[str]) -> float:
    doc_occurrences = sum(
        1
        for doc in corpus
        if term in re.split(pattern=r"\W", string=doc, flags=re.IGNORECASE)
    )
    return log2(len(corpus) / doc_occurrences)


def get_tf_idf(term: str, doc: str, corpus: list[str]):
    return get_tf(term, doc) * get_idf(term, corpus)


if __name__ == "__main__":
    print(get_tf(term="I", doc="I am a boy or I am a girl"))
    print(get_idf(term="a", corpus=["I am a boy and I am a girl", "Ramu is a boy"]))
