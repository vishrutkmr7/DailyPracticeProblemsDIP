"""
You are given two bounds, lower and upper and a sorted integer array, nums. Return a list of strings that represents the
missing ranges between lower and upper that are not covered in nums.

Ex: Given the following nums, lower, and upper…

nums = [2, 5, 7], lower = 0, upper = 10, return ["0->1","3->4","6","8->10"] (0 - 1, 3 - 4, 6, and 8 - 10 are not covered in
nums).
Ex: Given the following nums, lower, and upper…

nums = [], lower = 15, upper = 20, return ["15->20"].
"""


class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        if not nums:
            return [f"{lower}->{upper}"] if lower != upper else [f"{lower}"]
        result = []
        if lower < nums[0]:
            result.append(
                f"{lower}->{nums[0] - 1}" if lower != nums[0] - 1 else f"{lower}"
            )
        result.extend(
            f"{nums[i] + 1}->{nums[i + 1] - 1}"
            if nums[i] + 1 != nums[i + 1] - 1
            else f"{nums[i] + 1}"
            for i in range(len(nums) - 1)
            if nums[i] + 1 < nums[i + 1]
        )
        if nums[-1] < upper:
            result.append(
                f"{nums[-1] + 1}->{upper}"
                if nums[-1] + 1 != upper
                else f"{nums[-1] + 1}"
            )
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMissingRanges([2, 5, 7], 0, 10))
    print(solution.findMissingRanges([], 15, 20))
