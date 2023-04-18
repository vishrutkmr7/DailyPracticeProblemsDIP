"""
You are given two string arrays, queries and words. For any string, s, f(s)
is equal to the number of times the smallest lexicographical characters
occurs in s. For each query, queries[i] count the total number of words where
f(queries[i]) < f(word) and return the answer as an array.
Note: Both queries and words will only contain lowercase alphabetical
characters and contain at most ten strings each.

Ex: Given the following queries and words…

queries = ["abc"], words = ["def"], return 0 ('a' and 'd' both occur
once so f("abc") and f("def") are equal).
Ex: Given the following queries and words…

queries = ["abc"], words = ["ddef", "xxyz"], return 2 ('a' appears
once and 'd' and 'x' appear twice so f("abc") is less than both f("ddef") and f("xxyz")).
"""


import bisect


class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries][0]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSmallerByFrequency(["abc"], ["def"]))
    print(solution.numSmallerByFrequency(["abc"], ["ddef", "xxyz"]))
