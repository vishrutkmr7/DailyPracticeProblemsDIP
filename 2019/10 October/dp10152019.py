# This problem was recently asked by Twitter:

# Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.
# Numbers are strings of these symbols in descending order. In some cases, subtractive notation is used to avoid repeated characters.
# The rules are as follows:
# 1.) I placed before V or X is one less, so 4 = IV (one less than 5), and 9 is IX (one less than 10)
# 2.) X placed before L or C indicates ten less, so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
# 3.) C placed before D or M indicates 100 less, so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).


class Solution:
    def value(self, r):
        if r == "I":
            return 1
        if r == "V":
            return 5
        if r == "X":
            return 10
        if r == "L":
            return 50
        if r == "C":
            return 100
        if r == "D":
            return 500
        if r == "M":
            return 1000
        return -1

    def romanToInt(self, s):
        # Fill this in.
        res = 0
        i = 0
        while i < len(s):
            s1 = self.value(s[i])
            if i + 1 < len(s):
                s2 = self.value(s[i + 1])
                if s1 >= s2:
                    res = res + s1
                    i += 1
                else:
                    res = res + s2 - s1
                    i += 2
            else:
                res = res + s1
                i += 1

        return res


n = "MCMX"
print(Solution().romanToInt(n))
# 1910
