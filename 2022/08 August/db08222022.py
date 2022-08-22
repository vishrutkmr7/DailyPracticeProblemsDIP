"""
This question is asked by Amazon.
Given two strings, passage and text return whether or not the characters in text can be used to form the given passage.
Note: Each character in text may only be used once and passage and text will only contain lowercase alphabetical characters.

Ex: Given the following passage and text…

passage = "bat", text = "cat", return false.
Ex: Given the following passage and text…

passage = "dog" text = "didnotgo", return true.
"""


class Solution:
    def can_form_passage(self, passage, text):
        """
        :param passage: string
        :param text: string
        :return: boolean
        """
        if len(passage) > len(text):
            return False
        for i in enumerate(passage):
            if passage[i[0]] in text:
                text = text.replace(passage[i[0]], "", 1)
            else:
                return False
        return True


# Test Cases
s = Solution()
print(s.can_form_passage("bat", "cat"))  # returns false
print(s.can_form_passage("dog", "didnotgo"))  # returns true
