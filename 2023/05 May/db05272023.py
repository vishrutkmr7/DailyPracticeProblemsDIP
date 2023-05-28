"""
There are N people (labeled one to N) and it’s possible that one of these people is a celebrity.
A celebrity is someone who knows no one else, but every other person knows about them.
You’re also given a two-dimensional integer array, gossip, where gossip[i] = [x, y] denoting that
person x knows about person y. Given N and the gossip between people, return the celebrity. If no
celebrity exists, return -1.

Ex: Given the following N and gossip…

N = 3, gossip = [[1, 3], [2, 3]], return 3 (everyone knows 3 and 3 knows no one).
Ex: Given the following N and gossip…

N = 4, gossip = [[2, 1], [3, 2], [4, 1]], return -1.
"""


class Solution:
    def findCelebrity(self, N: int, gossip: list[list[int]]) -> int:
        adj = [set() for _ in range(N + 1)]
        for x, y in gossip:
            adj[x].add(y)

        candidates = list(range(1, N + 1))
        while len(candidates) > 1:
            person1 = candidates.pop()
            person2 = candidates.pop()

            if person2 in adj[person1]:
                candidates.append(person2)
            else:
                candidates.append(person1)

        if candidates:
            potential_celebrity = candidates[0]

            if adj[potential_celebrity]:
                return -1

            return next(
                (
                    -1
                    for i in range(1, N + 1)
                    if i != potential_celebrity and potential_celebrity not in adj[i]
                ),
                potential_celebrity,
            )

        return -1


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.findCelebrity(3, [[1, 3], [2, 3]]))
    print(solution.findCelebrity(4, [[2, 1], [3, 2], [4, 1]]))
