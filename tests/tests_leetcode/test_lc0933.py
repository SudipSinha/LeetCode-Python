from leetcode import lc0933


def test_RecentCounter():
    recentCounter = lc0933.RecentCounter()
    assert recentCounter.ping(1) == 1  # requests = [1], range is [-2999,1], return 1
    assert (
        recentCounter.ping(100) == 2
    )  # requests = [1, 100], range is [-2900,100], return 2
    assert (
        recentCounter.ping(3001) == 3
    )  # requests = [1, 100, 3001], range is [1,3001], return 3
    assert (
        recentCounter.ping(3002) == 3
    )  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
