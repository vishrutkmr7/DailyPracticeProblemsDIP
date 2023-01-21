"""
Given a sorted character array, letters, and a character, target, return the smallest character in
letters that is strictly larger than target.
Note: Letters wrap around. If target is ’y’ and letters contains ’c’ and ’d’, return ’c’.
Ex: Given the following letters and target…

letters = ['a', 'b', 'c'], target = 'b', return 'c'.
Ex: Given the following letters and target…

letters = ['r', 'y'], target = 'z', return 'r'.
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        for letter in letters:
            if letter > target:
                return letter


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreatestLetter(["a", "b", "c"], "b"))
    print(solution.nextGreatestLetter(["r", "y"], "z"))
