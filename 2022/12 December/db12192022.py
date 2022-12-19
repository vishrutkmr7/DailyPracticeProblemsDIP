"""
Given a string s and a string p, return all the starting indices of p’s anagrams within s.
Note: Both strings will contain at least one character and will only contain lowercase alphabetical
characters.

Ex: Given the following s and p…

s = "abcbabc", p = "abc", return [0, 2, 4].
Ex: Given the following s and p…

s = "abc", p = "def", return [].
"""


from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        hashMap = defaultdict(int)
        if len(p) > len(s):
            return []
        for char in p:
            hashMap[char] += 1

        for i in range(len(p) - 1):
            if s[i] in hashMap:
                hashMap[s[i]] -= 1

        for i in range(-1, len(s) - len(p) + 1):
            if i > -1 and s[i] in hashMap:
                hashMap[s[i]] += 1
            if i + len(p) < len(s) and s[i + len(p)] in hashMap:
                hashMap[s[i + len(p)]] -= 1

            if not any(hashMap.values()):
                result.append(i + 1)

        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("abcbabc", "abc"))
    print(solution.findAnagrams("abc", "def"))
