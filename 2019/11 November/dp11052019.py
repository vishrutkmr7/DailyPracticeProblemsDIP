# This problem was recently asked by Amazon:

# Version numbers are strings that are used to identify unique states of software products.
# A version number is in the format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots.
# These generally represent a hierarchy from major to minor changes. Given two version numbers version1 and version2,
# conclude which is the latest version number. Your code should do the following:
# If version1 > version2 return 1.
# If version1 < version2 return -1.
# Otherwise return 0.

from packaging import version


class Solution:
    def compareVersion(self, version1, version2):
        # Fill this in.
        v1 = version.parse(version1)
        v2 = version.parse(version2)
        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
        else:
            return 0


version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
