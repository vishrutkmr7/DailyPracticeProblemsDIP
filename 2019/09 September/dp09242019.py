# This problem was recently asked by Facebook:

# Given a string, you need to reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, str):
        # Fill this in.
        temp = str.split()
        finalStr = ""
        for i in range(len(temp)):
            rev = "".join(reversed(temp[i]))
            if i == 0:
                finalStr = rev
            else:
                finalStr += f" {rev}"

        return finalStr


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
