"""
You are given a list of words and asked to find the longest chain. Two words (or more) form a
chain if a single letter can be added anywhere in a word, s, to form a word, t (where s and t
are both words within the list of words you’re given). Return the length of the longest chain
you can form.

Ex: Given the following words…

words = ["a", "ab", "abc"], return 3 ("a" can be transformed to "ab" by adding a "b" and "ab"
can be transformed by adding a "c" giving a chain length of 3).
Ex: Given the following words…

words = ["a", "abc"], return 1 (both "a" or "abc" form their own chains of size one, they
cannot be added together).
"""


class Solution:
    def longestStrChain(self, words):
        # Time O(nlogn) Space O(n)
        words.sort(key=len)
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1 :]
                if new_word in dp:
                    dp[word] = max(dp[word], dp[new_word] + 1)
        return max(dp.values())


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestStrChain(["a", "ab", "abc"]))  # 3
    print(sol.longestStrChain(["a", "abc"]))  # 1
