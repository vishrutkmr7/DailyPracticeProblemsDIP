"""
Given a string s that contains only the following characters: (, ), and *,
where asterisks can represent either an opening or closing parenthesis, return whether or not
the string can form a valid set of parentheses.

Ex: Given the following string s…

s = "*)", return true.
Ex: Given the following string s…

s = "(**)", return true.
Ex: Given the following string s…

s = "((*", return false.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # O(n) time | O(1) space
        low = 0
        high = 0

        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkValidString("*)"))
    print(solution.checkValidString("(**)"))
    print(solution.checkValidString("((*"))
