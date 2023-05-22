"""
Given an integer array, salaries, salaries[i] represents the salary of the ith employee.
Return the average employee salary not considering the largest or the smallest salary.

Ex: Given the following salaries…

salaries = [5000, 2000, 3000, 4000], return 3500.00000 ((3000 + 4000) / 2).
"""


class Solution:
    def average(self, salaries):
        salaries.sort()
        salaries.pop(0)
        salaries.pop(-1)
        return sum(salaries) / len(salaries)


# Test Cases
if __name__ == "__main__":
    s = Solution()
    print(s.average([5000, 2000, 3000, 4000]))  # 3500.00000
