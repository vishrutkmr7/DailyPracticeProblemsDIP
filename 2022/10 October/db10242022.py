"""
Given a list of strings, return a list of strings containing all anagrams grouped together.

Ex: Given the following list of strings strs…

strs = ["car", "arc", "bee", "eeb", "tea"], return
[
  ["car","arc"],
  ["tea"],
  ["bee","eeb"]
]
"""


from functools import reduce


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return list(
            reduce(
                lambda acc, x: {**acc, x[0]: [x[1], *acc.get(x[0], [])]},
                ((tuple(sorted(s)), s) for s in strs),
                {},
            ).values()
        )


if __name__ == "__main__":
    strs = ["car", "arc", "bee", "eeb", "tea"]
    print(Solution().groupAnagrams(strs))
