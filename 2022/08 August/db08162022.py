"""
This question is asked by Microsoft.
Implement a trie class that supports insertion and search functionalities.
Note: You may assume only lowercase alphabetical characters will added to your trie.

Ex: Given the following operations on your trie…

Trie trie = new Trie()
trie.insert("programming");
trie.search("computer") // returns false.
trie.search("programming") // returns true.
"""


class Trie:
    def __init__(self):
        self.words = []

    def insert(self, word):
        self.words.append(word)

    def search(self, word):
        return word in self.words


# Test Cases
trie = Trie()
trie.insert("programming")
print(trie.search("computer"))  # returns false.
print(trie.search("programming"))  # returns true.
