"""
You are given an array of interval objects, which each consist of a start time and an end time.
Each interval object represents when a particular meeting starts and ends. Return whether or not
someone could attend every meeting.

Ex: Given the following intervals...

intervals = [[1, 3], [5, 10]], return true.
Ex: Given the following intervals...

intervals = [[1, 8], [5, 9]], return false.
"""


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        return all(
            intervals[i][0] >= intervals[i - 1][1] for i in range(1, len(intervals))
        )
