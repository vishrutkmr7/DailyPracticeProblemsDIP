# This problem was recently asked by Facebook:

# Given a string, you need to reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, str):
        # Fill this in.
        temp = str.split()
        res = []
        for word in temp:
            rev = "".join(reversed(word))
            res.append(rev)
        finalStr = ""
        for i in range(0, len(res)):
            if i == 0:
                finalStr = res[i]
            else:
                finalStr += " " + res[i]

        return finalStr


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
