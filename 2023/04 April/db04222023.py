"""
You are given a two-dimensional matrix that represents the grades of a class of students.
Each grade is represented as an array where the first index is the student’s ID and the
second student is a grade (0 - 100) that the student has received. Given these grades,
calculate the average of each student’s top five scores and return the result.
Note: Each student is guaranteed to have at least 5 scores. Student IDs start from zero
and increase by one. Your return variable should be sorted according to student ID.

Ex: Given the following grades…

grades = [[1, 100], [1, 50], [2, 100], [2, 93], [1, 39], [2, 87], [1, 89], [1, 87],
[1, 90], [2, 100], [2, 76]], return [[1, 83], [2, 91]] (Student one's average is an 83
and student two's average is a 91).
"""


class Solution:
    def highFive(self, grades: list[list[int]]) -> list[list[int]]:
        student_grades = {}
        for student, grade in grades:
            if student not in student_grades:
                student_grades[student] = []
            student_grades[student].append(grade)
        return [
            [student, sum(sorted(student_grades[student], reverse=True)[:5]) // 5]
            for student in sorted(student_grades.keys())
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.highFive(
            [
                [1, 100],
                [1, 50],
                [2, 100],
                [2, 93],
                [1, 39],
                [2, 87],
                [1, 89],
                [1, 87],
                [1, 90],
                [2, 100],
                [2, 76],
            ]
        )
    )
