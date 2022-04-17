# This problem was recently asked by AirBNB:

# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.


class Solution:
    def buddyStrings(self, A, B):
        # Fill this in.
        if len(A) != len(B):
            return False

        prev = -1
        curr = -1
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                if count > 2:
                    return False
                prev = curr
                curr = i
        # Check if previous unmatched of A
        # is equal to curr unmatched of B
        # and also check for curr unmatched character,
        # if both are same, then return true
        return count == 2 and A[prev] == B[curr] and A[curr] == B[prev]


print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))
# True
print(Solution().buddyStrings("aaaaaabbc", "aaaaaaacb"))
# False
