"""You are typing on a computer when all of a sudden you realize you’ve been typing with caps lock on. Given a string s,
return a new string containing all of its alphabetical character transformed to lowercase.
Note: Do you not use an built in library functions. 

Ex: Given the following string s…

s = "ABC", return "abc".
Ex: Given the following string s…

s = "ABCa", return "abca".
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        h = dict(zip(upper, lower))

        return "".join([h.get(x, x) for x in s])


# Test Cases
s = Solution()
assert s.toLowerCase("ABC") == "abc"
assert s.toLowerCase("ABCa") == "abca"
print("All Tests Passed!")
