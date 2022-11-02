"""
Given a list of interval object, merge all overlapping intervals and return the result.
Note: an interval object is a simple object that contains a start time and end time and
can be constructed by passing a starting and ending time to the constructor.

Ex: Given the following intervals...

intervals = [[1, 3], [1, 8]], return a list of interval objects containing [[1, 8]].
Ex: Given the following intervals...

intervals = [[1, 2], [2, 6], [7 ,10]], return a list of interval objects containing [[1, 6], [7, 10]].
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1, 3], [1, 8]]))
    print(solution.merge([[1, 2], [2, 6], [7, 10]]))
