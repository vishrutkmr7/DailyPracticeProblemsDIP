"""
This question is asked by Facebook.
Given an integer N, where N represents the number of pairs of parentheses
(i.e. ”(“ and ”)”) you are given, return a list containing all possible well-formed parentheses you can create.

Ex: Given the following value of N…

N = 3
return [  
    "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):

        res = []

        def dfs(path, left, right):
            if left > n or right > n:
                return

            if left == right == n:
                res.append(path)
                return

            if left > right:
                dfs(f"{path}(", left + 1, right)
                dfs(f"{path})", left, right + 1)

            else:
                dfs(f"{path}(", left + 1, right)

        dfs("", 0, 0)
        return res


# Test Cases
print(Solution().generateParenthesis(3))
