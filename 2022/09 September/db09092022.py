"""
This question is asked by Facebook.
Given a string, check if it can be modified such that no two adjacent characters are the same.
If it is possible, return any string that satisfies this condition and if it is not possible return an empty string.

Ex: Given the following string s…

s = "abb", return "bab".
Ex: Given the following string s…

s = "xxxy", return "" since it is not possible to modify s such that no two adjacent characters are the same.
"""


from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        maps = Counter(s)
        li = [[-val, key] for key, val in maps.items()]
        heapq.heapify(li)
        prev = None
        res = ""

        while li or prev:
            if prev and not li:
                return ""
            cnt, char = heapq.heappop(li)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(li, prev)
                prev = None

            if cnt:
                prev = [cnt, char]

        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.reorganizeString("abb"))
    print(solution.reorganizeString("xxxy"))
