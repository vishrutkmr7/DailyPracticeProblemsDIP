"""
You are given a code and asked to modify the code to unlock a vault. In addition to the code,
you’re also given a value k. To unlock the vault, you must modify each value in code based on
the value of k. If k > 0, you must replace the ith value with the sum of the next k values.
If k < 0, you must replace the ith value with the sum of the previous k values. If k == 0,
you must replace the ith value with the number zero. Return the correct code to unlock the vault.
Note: Values in code are circular meaning that the “next” value after the last value in code
is the first value in code and similarly, the previous value to the first value in code is
the last value in code.

Ex: Given the following code and value k…

code = [1, 2, 3], k = 2, return [5, 4, 3] (2 + 3, 3 + 1, 1 + 2).
Ex: Given the following code and value k…

code = [4, 1, 3], k = -1, return [3, 4, 1].
"""


class Solution:
    def unlock(self, code: list[int], k: int) -> list[int]:
        """
        Unlocks the vault given a code and a value k.

        Args:
          code: A list of integers representing the code.
          k: An integer representing the value of k.

        Returns:
          A list of integers representing the unlocked code.
        """

        # Check if k is positive, negative, or zero.
        if k > 0:
            # If k is positive, then we need to replace each value in code with the sum of the next k values.
            unlocked_code = []
            for i in range(len(code)):
                start_index = i + 1
                end_index = i + k
                end_index = min(end_index, len(code))
                unlocked_code.append(sum(code[start_index:end_index]))
        elif k < 0:
            # If k is negative, then we need to replace each value in code with the sum of the previous k values.
            unlocked_code = []
            for i in range(len(code)):
                start_index = i - k
                start_index = max(start_index, 0)
                end_index = i
                unlocked_code.append(sum(code[start_index:end_index]))
        else:
            # If k is zero, then we need to replace each value in code with the number zero.
            unlocked_code = [0] * len(code)

        return unlocked_code


# Test Cases
if __name__ == "__main__":
    s = Solution()
    print(s.unlock([1, 2, 3], 2))
    print(s.unlock([4, 1, 3], -1))
