"""149. Max Points on a Line

Link: https://leetcode.com/problems/max-points-on-a-line/

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
"""

from collections import defaultdict
from fractions import Fraction
from math import inf, isfinite


class Solution:
    @staticmethod
    def _get_2Dline_parameters(
        point1: tuple[int, int], point2: tuple[int, int]
    ) -> tuple[Fraction | float, Fraction]:
        (x1, y1) = point1
        (x2, y2) = point2
        slope = Fraction(y2 - y1, x2 - x1) if x1 != x2 else inf  # slope
        intercept = (
            y1 - slope * x1 if x1 != x2 else Fraction(x1, 1)  # type: ignore
        )  # y-intercept or x-intercept
        return (slope, intercept)  # type: ignore

    def maxPoints_line_2d(self, points: list[tuple[int, int]]) -> int:
        """Idea: a line can be uniquely identified by its intercept and slope.
        Time complexity: O(n^2), space complexity: O(1).
        """
        if not points:
            return 0
        elif len(points) <= 2:
            return len(points)

        lines: defaultdict[tuple[Fraction | float, Fraction], int] = defaultdict(int)
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                (slope, intercept) = Solution._get_2Dline_parameters(
                    points[i], points[j]
                )
                lines[(slope, intercept)] += 1

        #   Winning line.
        (winner_slope, winner_intercept) = max(lines, key=lambda key: lines[key])

        #   How many points fall on this line?
        count = 0
        for point in points:
            if (
                isfinite(winner_slope)
                and point[1] == winner_intercept + winner_slope * point[0]
            ) or (not isfinite(winner_slope) and point[0] == winner_intercept):
                count += 1

        return count
