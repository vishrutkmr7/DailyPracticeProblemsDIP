"""
Given an encoded string, s, return its decoded representation. The string s will be encoded
as follows N[letters], meaning that the letters should be repeated N times in the decoded
representation.
Note: You may assume s always encoded correctly (i.e. correct formatting of brackets, only
positive values outside the brackets, and always lowercase alphabetical characters inside the
brackets).

Ex: Given the following string s…

s = "3[a]2[b]1[c]", return "aaabbc" ("a" is repeated 3 times, "b" is repeated 2 times, and "c"
is repeated 1 time).
"""


class Solution:
    def decodeString(self, s):
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
        return "".join(stack)


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[b]1[c]"))  # aaabbc
