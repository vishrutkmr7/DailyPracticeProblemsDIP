"""
Given a string, s, return the total number of substrings that only contain one distinct character.

Ex: Given the following string s…

s = "aabbc", return 7. ("a", "aa", "a", "b", "bb", "b", "c").
Ex: Given the following string s…

s = "aaa", return 6.
"""


class Solution:
    def countSubstrings(self, s: str, k: int) -> int:
        N = len(s)

        count = 0
        store = {}
        for i in range(k):
            store[s[i]] = store.get(s[i], 0) + 1

        if len(store) == k:
            count += 1

        for i in range(k, N):
            store[s[i]] = store.get(s[i], 0) + 1

            store[s[i - k]] -= 1

            if store[s[i - k]] == 0:
                del store[s[i - k]]

            if len(store) == k:
                count += 1

        return count


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("aabbc", 1))
    print(sol.countSubstrings("aaa", 1))
