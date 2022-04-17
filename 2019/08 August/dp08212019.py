# This problem was recently asked by Twitter:

# Given a string with the initial condition of dominoes, where:

# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side

# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

class Solution(object):
    def pushDominoes(self, dominoes):
        # Fill this in.
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        # print(symbols)
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            for k in range(i+1, j):
                if x == y:
                    ans[k] = x
                elif x > y: #RL
                    ans[k] = '.LR'[(k-i > j-k) - (k-i < j-k)] # cmp : (a > b) - (a < b)

        return "".join(ans)

print (Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
