"""
This question is asked by Amazon.
Given a valid IP address, defang it.
Note: To defang an IP address, replace every ”.”, with ”[.]”.

Ex: Given the following address…

address = "127.0.0.1", return "127[.]0[.]0[.]1"
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.defangIPaddr("127.0.0.1") == "127[.]0[.]0[.]1"
    print("All tests passed.")
