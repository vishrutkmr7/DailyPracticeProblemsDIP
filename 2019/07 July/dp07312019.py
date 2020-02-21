# Given a string, s, find the longest palindromic substring in s. [Asked for Twitter interview]


class Solution:
    def longestPalindrome(self, s):
        # Fill this in.
        maxLength = 1  # for every 1 letter word is a palindrome.. duh!
        start = 0
        Len = len(s)

        low = 0
        high = 0

        for i in range(1, Len):

            # even lengthed palindromes...
            low = i - 1
            high = i

            while low >= 0 and high < Len and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

            # odd lengthed palindromes...
            low = i - 1
            high = i + 1
            while low >= 0 and high < Len and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

        return s[start : start + maxLength]


# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
