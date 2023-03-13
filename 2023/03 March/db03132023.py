"""
You are given a string, s, where each character in the string is either 'U' (Up) or 'D' (Down).
Return any permutation of an array, A, such that for every index in the array where
s[i] == U then A[i] < A[i + 1] and for every index where s[i] == D then A[i] > A[i + 1].

Ex: Given the following string s…

s = "UD", you could return [0, 2, 1] (0 is less than 1, 2 is greater than 1).
Ex: Given the following string s…

s = "DUU", you could return [3,0,1,2]
"""


class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        if not s:
            return []
        if len(s) == 1:
            return [0]
        result = []
        left = 0
        right = len(s)
        for val in s:
            if val == "U":
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        result.append(left)
        return result


# Test Cases
if __name__ == "__main__":
    s = "UD"
    print(Solution().diStringMatch(s))
    s = "DUU"
    print(Solution().diStringMatch(s))
