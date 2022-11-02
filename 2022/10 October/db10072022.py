"""
High school students are voting for their class president and you’re tasked with counting the votes.
Each presidential candidates is represented by a unique integer and the candidate that should win the election
is the candidate that has received more than half the votes. Given a list of integers, return the candidate that should become the class president.
Note: You may assume there is always a candidate that has received more than half the votes.

Ex: Given the following votes…

votes = [1, 1, 2, 2, 1], return 1.
Ex: Given the following votes…

votes = [1, 3, 2, 3, 1, 2, 3, 3, 3], return 3.
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) // 2]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.majorityElement([1, 1, 2, 2, 1]) == 1
    assert solution.majorityElement([1, 3, 2, 3, 1, 2, 3, 3, 3]) == 3
    print("All tests passed.")
