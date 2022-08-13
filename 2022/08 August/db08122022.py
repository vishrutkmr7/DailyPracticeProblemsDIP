"""
This question is asked by Facebook.
Releasing software can be tricky and sometimes we release new versions of our software with bugs.
When we release a version with a bug it’s referred to as a bad release.
Your product manager has just informed you that a bug you created was released in one of the
past versions and has caused all versions that have been released since to also be bad.
Given that your past releases are numbered from zero to N and you have a helper function
isBadRelease(int releaseNumber) that takes a version number and returns a boolean
as to whether or not the given release number is bad, return the release number that
your bug was initially shipped in.

Note: You should minimize your number of calls made to isBadRelease().

Ex: Given the following value N…

N = 5 and release number four is the release your bug was shipped in...
isBadRelease(3) // returns false.
isBadRelease(5) // returns true.
isBadRelease(4) // returns true.

return 4.
"""


class Solution:
    def findBadRelease(self, n):
        low, mid, high = 1, n // 2, n
        while low <= high:
            mid = (low + high) // 2
            if self.isBadRelease(mid):
                if not (self.isBadRelease(mid - 1)):
                    break
                high = mid - 1
            else:
                low = mid + 1
        return mid if mid > 0 else 1

    def isBadRelease(self, releaseNumber):
        # Write your code here
        badDb = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: True,
            5: True,
        }
        return badDb[releaseNumber]


# Test Cases
print(Solution().findBadRelease(5))
