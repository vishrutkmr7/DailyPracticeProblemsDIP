"""
You and a friend are trying to choose a restaurant to go to. You both give your preferences
of restaurants in separate lists. You need to find a restaurant to go to that’s listed in
both of your preferences that has the least index sum. If there are ties, output all
restaurants you could go to together.

Ex: Given the following lists...

list1 = ["A", "B", "C", "D"], list2 = ["D", "B", "C"], return [“B”]
(“B” is the least index sum 1 + 1 whereas “D” is 3 + 0).
Ex: Given the following lists...

list1 = [“C”], list2 = [“D”], return [].
"""


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Time: O(n)
        # Space: O(n)
        dict1 = {list1[i]: i for i in range(len(list1))}
        dict2 = {list2[i]: i for i in range(len(list2))}
        min_sum = float("inf")
        for key in dict1:
            if key in dict2:
                min_sum = min(min_sum, dict1[key] + dict2[key])
        return [
            key
            for key, value in dict1.items()
            if key in dict2 and value + dict2[key] == min_sum
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRestaurant(["A", "B", "C", "D"], ["D", "B", "C"]))
    print(solution.findRestaurant(["C"], ["D"]))
