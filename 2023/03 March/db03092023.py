"""
You are typing on a broken keyboard trying to spell your friend’s name.
Since the keyboard is broken, sometimes when you press a key the key is typed one or more times.
Given a string typed and a string namereturn whether or not you’ve successfully typed your friend’s
name even though certain keys might be repeated.
Note: Both strings will only contain lowercase alphabetical characters.

Ex: Given the following typed and name…

typed = "kkevin", name = "kevin", return true.
Ex: Given the following typed and name…

typed = "timmm", name = "timmy", return false.
"""


class Solution:
    def isName(self, typed: str, name: str) -> bool:
        i = 0
        for index, value in enumerate(typed):
            if i < len(name) and name[i] == value:
                i += 1
            elif index == 0 or value != typed[index - 1]:
                return False
        return i == len(name)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isName("kkevin", "kevin") is True
    assert solution.isName("timmm", "timmy") is False
    print("All tests passed successfully.")
