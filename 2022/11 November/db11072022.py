"""
You are given a list of values and a list of labels. The ith element in labels represents
the label of the ith element. Similarly, the ith element in values represents
the value associated with the ith element (i.e. together, an “item” could be thought of
as a label and a price). Given a list of values, a list of labels, a limit, and wanted,
return the sum of the most expensive items you can group such that the total number
of items used is less than wanted and the number of any given label that is used is less than limit. 

Ex: Given the following variables...

values = [5,4,3,2,1]
label = [1,1,2,2,3]
wanted = 3
limit = 1
return 9 (the sum of the values associated with the first, third, and fifth items).
"""


class Solution:
    """Solution"""

    def most_expensive(
        self, values: list[int], labels: list[int], wanted: int, limit: int
    ) -> int:
        """Return the sum of the most expensive items you can group"""
        if not values or not labels or not wanted or not limit:
            return 0

        items = sorted(zip(values, labels), reverse=True)
        label_count = {}
        total = 0

        for value, label in items:
            if wanted == 0:
                break

            if label_count.get(label, 0) < limit:
                total += value
                label_count[label] = label_count.get(label, 0) + 1
                wanted -= 1

        return total


# Test Cases
if __name__ == "__main__":
    SOLUTION = Solution()
    assert SOLUTION.most_expensive([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1) == 9
    print("All examples passed!")
