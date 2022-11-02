"""
Given a string s, remove the minimum number of parentheses to make s valid.
Return all possible results.

Ex: Given the following string s...

s = "(()()()", return ["()()()","(())()","(()())"].
Ex: Given the following string s...

s = "()()()", return ["()()()"].
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        if not s:
            return [""]
        result = []
        self.remove(s, result, 0, 0, ("(", ")"))
        return result

    def remove(self, s, result, last_i, last_j, par):
        stack = 0
        for i in range(last_i, len(s)):
            if s[i] == par[0]:
                stack += 1
            if s[i] == par[1]:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1 :], result, i, j, par)
            return
        reversed_s = s[::-1]
        if par[0] == "(":
            self.remove(reversed_s, result, 0, 0, (")", "("))
        else:
            result.append(reversed_s)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeInvalidParentheses("(()()()"))
    print(solution.removeInvalidParentheses("()()()"))
