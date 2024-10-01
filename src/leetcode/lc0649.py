"""Dota2 Senate

Link: https://leetcode.com/problems/dota2-senate/

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string `senate` representing each senator's party belonging. The character `'R'` and `'D'` represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be `"Radiant"` or `"Dire"`.
"""

from collections import defaultdict, deque


def predictPartyVictory(senate: str) -> str:
    order = list(senate)
    name = {
        "R": "Radiant",
        "D": "Dire",
    }
    opposition = {
        "R": "D",
        "D": "R",
    }

    order_party: defaultdict[str, deque[int]] = defaultdict(deque[int])
    for idx, party in enumerate(order):
        order_party[party].append(idx)
    while order_party["R"] and order_party["D"]:
        list_ban_round = []
        idx = 0
        while idx < len(order):
            if idx in list_ban_round:  # Skip banned voter in this round.
                idx += 1
                continue
            party_cur = order[idx]
            if len(order_party[opposition[party_cur]]) > 0:
                list_ban_round.append(order_party[opposition[party_cur]].popleft())
                idx += 1
            else:
                return name[party_cur]
        order = [order[idx] for idx in range(len(order)) if idx not in list_ban_round]
        order_party = defaultdict(deque[int])
        for idx, party in enumerate(order):
            order_party[party].append(idx)
    return name["D"] if len(order_party["R"]) == 0 else name["R"]
