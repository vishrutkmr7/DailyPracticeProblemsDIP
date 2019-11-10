# This problem was recently asked by Amazon:

# MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc.
# In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth.
# Given a positive integer, find its corresponding column name. (Update: and Vice-versa: 11/09/2019 Solution)

import string


class Solution:
    def convertToTitle(self, n):
        # Fill this in.
        ans = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            ans = chr(65 + remainder) + ans
        return ans

    def convertToNum(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord("A")) + 1
        return num


input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
input4 = "Z"
input5 = "AA"
input6 = "ABY"
print(Solution().convertToNum(input4))
# 26
print(Solution().convertToNum(input5))
# 27
print(Solution().convertToNum(input6))
# 753
