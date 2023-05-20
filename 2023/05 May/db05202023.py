"""
A restaurant offers two potential sides to their dishes, soup or salad. You are given two integer
arrays, customers and sides. The customers array contains only ones and zeroes where v
represents the ith customer’s choice: zero being a preference of soup and one being a preference
of salad. Similarly, the sides array represents the sides that are available: zero represents a
soup and one represents a salad. All the customers are standing in line to receive a side dish.
All the side dishes in sides must be removed in order (i.e. the first side dish must be given to
a customer before the next one can be given to a customer). If the customer at the front of the
line’s preference aligns with the side dish that’s available, the customer can take the side dish
and go to their table. If their preference does not align, the current side dish remains and the
customer goes to the back of the line. Continuing this process, it is possible that some customers’
preferences are never satisfied. Return the number of customers who could not receive their
preferred side dish.

Ex: Given the following customers and sides…

customers = [1, 1, 1], sides = [1, 1, 1], return 0 (all customers' preferences were satisfied, they
all received salad).
Ex: Given the following customers and sides…

customers = [1, 0, 1], sides = [0, 0, 1], return 2 (first customer passes on the available soup,
second customer takes the soup, then neither remaining customer wants the second soup).
"""


class Solution:
    def unsatisfied_customers(self, customers, sides):
        unsatisfied = 0
        for customer in customers:
            if not sides or customer != sides[0]:
                unsatisfied += 1
            else:
                sides.pop(0)
        return unsatisfied


# Test Cases
if __name__ == "__main__":
    s = Solution()
    print(s.unsatisfied_customers([1, 1, 1], [1, 1, 1]))
    print(s.unsatisfied_customers([1, 0, 1], [0, 0, 1]))
