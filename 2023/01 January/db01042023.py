"""
You are given a string, attendance that represents a student’s class attendance throughout the semester.
A student can be marked, A for absent, L, for late, or P for present. To get credit for the class,
a student cannot miss more than one class and cannot come late to class twice in a row. Given the
current students attendance record, return whether or not the student has passed the class.

Ex: Given the following attendance of a student…

attendance = "PLPAPPPA", return false.
Ex: Given the following attendance of a student…

attendance = "PLPLPLPALP", return true.
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if s.count("A") > 1 else "LL" not in s


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.checkRecord("PLPAPPPA") is False
    assert solution.checkRecord("PLPLPLPALP") is True
    print("All tests passed.")
