"""
This question is asked by Facebook.
You are given a two dimensional matrix,friends, that represents relationships between coworkers in an office.
If friends[i][j] = 1 then coworker i is friends with coworker j and coworker j is friends with coworker i.
Similarly if friends[i][j] = 0 then coworker i is not friends with coworker j and coworker j is not friend with coworker i.
Friendships in the office are transitive (i.e. if coworker one is friends with coworker two
and coworker two is friends with coworker three, coworker one is also friends with coworker three).
Given the friendships in the office defined by friends, return the total number of distinct friends groups in the office.
Note: Each coworker is friends with themselves (i.e.matrix[i][j] = 1 for all values where i = j)

Ex: Given the following matrix friends…

friends = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
], return 2.
The 0th and 1st coworkers are friends with one another (first friend group).
The 2nd coworker is friends with thyself (second friend group).
"""


class Solution:
    def find_groups(self, friends):
        # Create a set of all the coworkers
        coworkers = set()
        for i in enumerate(friends):
            for j in enumerate(i[1]):
                if friends[i[0]][j[0]] == 1:
                    coworkers.add(i[0])
                    coworkers.add(j[0])
        # Create a set of all the friend groups
        friend_groups = set()
        for i in enumerate(friends):
            if i[0] in coworkers:
                friend_groups.add(i[0])
                for j in range(len(friends[i[0]])):
                    if friends[i[0]][j] == 1 and j in coworkers:
                        friend_groups.add(j)
        return len(friend_groups)


# Test Cases
s = Solution()
friends = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(s.find_groups(friends))  # returns 2.
