"""
Given a string, s, make it acceptable. An acceptable string is a string that contains
no two adjacent characters that are the same with one letter being capitalized
and the other being lowercased.
Note: An empty string is acceptable and only one distinct answer will exist.

Ex: Given the following string s…

s = "Aabb", return "bb".
Ex: Given the following string s…

s = "AabBcC", return "".
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and abs(ord(ch) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.makeGood("Aabb"))
    print(solution.makeGood("AabBcC"))
