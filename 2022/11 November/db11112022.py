"""
Your friend has created a secret encrypted language by shifting letters around
in the English alphabet. Given the new order of the letters and a list of words,
return whether or not your friend has sorted the words lexicographically.

Ex: Given the following order and words...

order = "worldabcefghijkmnpqstuvxyz"
words = ["word","world","row"]
return false since ‘d’ comes before ‘l’ in the new language’s ordering and
therefore the first and second word are not sorted correctly.
"""


class Solution:
    def isSorted(self, order: str, words: list[str]) -> bool:
        """Returns whether or not words are sorted"""
        hmap = {c: i for i, c in enumerate(order)}
        words = [[hmap[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.isSorted("worldabcefghijkmnpqstuvxyz", ["word", "world", "row"])
        is False
    )
    print("All tests passed.")
