"""
This question is asked by Facebook.
Given a character array, compress it in place and return the new length of the array.
Note: You should only compress the array if its compressed form will be at least as short as the length of its original form.

Ex: Given the following character array chars…

chars = ['a', 'a', 'a', 'a', 'a', 'a'], return 2.
chars should be compressed to look like the following:
chars = ['a', '6']
Ex: Given the following character array chars…

chars = ['a', 'a', 'b', 'b', 'c', 'c'], return 6.
chars should be compressed to look like the following:
chars = ['a', '2', 'b', '2', 'c', '2']
Ex: Given the following character array chars…

chars = ['a', 'b', 'c'], return 3.
In this case we chose not to compress chars."""


class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        c, n, k = chars[0], 1, 0  # char, number of char, index
        for i in range(1, len(chars)):
            if chars[i] == c:
                n += 1
            else:
                s = [c] + list(str(n)) if n > 1 else [c]
                chars[k : k + len(s)] = s
                k += len(s)
                c, n = chars[i], 1
        s = [c] + list(str(n)) if n > 1 else [c]
        chars[k : k + len(s)] = s
        k += len(s)
        return k


# Test Cases
sol = Solution()
print(sol.compress(["a", "a", "a", "a", "a", "a"]))  # returns 2
print(sol.compress(["a", "a", "b", "b", "c", "c"]))  # returns 6
print(sol.compress(["a", "b", "c"]))  # returns 3
