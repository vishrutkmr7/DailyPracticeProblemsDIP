"""
Students in a class are lining up in ascending height order, but are having some trouble doing so.
Because of this, it’s possible that some students might be out of order. In particular,
a student that is taller than both their neighboring students (i.e. the person to both
their left and right) sticks out like a sore thumb. Given an integer array that represents
each students height, return the index of a “sore thumb”.
Note: If there are multiple sore thumbs you may return the index of any of them.
All numbers in the array will be unique. You may assume that to the left and right bounds
of the array negative infinity values exist. 

Ex: Given the following students...

students = [1, 2, 3, 7, 5], return 3.
"""


class Solution:
    def soreThumb(self, students):
        return next(
            (
                i
                for i in range(1, len(students) - 1)
                if students[i] > students[i - 1] and students[i] > students[i + 1]
            ),
            -1,
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.soreThumb([1, 2, 3, 7, 5]))
