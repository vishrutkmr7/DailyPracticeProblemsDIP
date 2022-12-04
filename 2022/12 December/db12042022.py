"""
Given a string, s, that represents a Roman numeral, return its associated integer value.
Note: You may assume that each string represents a valid Roman numeral and its value will
not exceed one thousand.
Ex: Given the following string s...

s = "DCLII", return 652.
Ex: Given the following string s...

s = "VIII", return 8.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum(
            roman[s[i]] - 2 * roman[s[i - 1]]
            if i > 0 and roman[s[i]] > roman[s[i - 1]]
            else roman[s[i]]
            for i in range(len(s))
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("DCLII"))
    print(solution.romanToInt("VIII"))
