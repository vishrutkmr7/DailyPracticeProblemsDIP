"""
You are given a list of strings, times, where each string represent a timestamp of a twenty-four hour
clock (i.e. hours and minutes - “HH:MM”). Return the minimum difference, in minutes, between any two
of the timestamps in the list.

Ex: Given the following times…

times = ["01:00", "01:10"], return 10 (i.e. there are 10 minutes between the two times).
Ex: Given the following times…

times = ["00:00", "12:23", "05:50", "23:12"], return 48.
"""


class Solution:
    def minTimeDifference(self, times):
        times = [int(time[:2]) * 60 + int(time[3:]) for time in times]
        times.sort()
        times.append(times[0] + 1440)
        return min(times[i + 1] - times[i] for i in range(len(times) - 1))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minTimeDifference(["01:00", "01:10"]))
    print(solution.minTimeDifference(["00:00", "12:23", "05:50", "23:12"]))
