"""
You are given a list of intervals as a two dimensional matrix. Each interval
contains two values, first a start time and second an end time. An interval
[a, b] is “covered” by another interval [c, d] if and only if c <= a and b <= d.
Given these intervals, return the count of intervals that are not covered by
any other interval.

Ex: Given the following intervals…

intervals = [[1, 2], [0, 4]], return 1 ([0, 4] is the only remaining interval).
Ex: Given the following intervals…

intervals = [[8, 10], [4, 6], [1, 2]], return 3.
"""


class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        end = 0
        for interval in intervals:
            if interval[1] > end:
                count += 1
                end = interval[1]
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeCoveredIntervals([[1, 2], [0, 4]]))
    print(solution.removeCoveredIntervals([[8, 10], [4, 6], [1, 2]]))
