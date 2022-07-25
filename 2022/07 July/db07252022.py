"""This question is asked by Amazon.
You’re running a popsicle stand where each popsicle costs $5.
Each customer you encountered pays with either a $5 bill,
a $10 bill, or a $20 bill and only buys a single popsicle.
The customers that come to your stand come in the ordered given by the customers array where
customers[i] represents the bill the ith customer pays with.
Starting with $0, return whether or not you can serve all the given customers
while also giving the correct amount of change.

Ex: Given the following customers…

customers = [5, 10], return true
collect $5 from the first customer, pay no change.
collet $10 from the second customer and give back $5 change.

Ex: Given the following customers…

customers = [10], return false
collect $10 from the first customer and we cannot give back change.

Ex: Given the following customers…

customers = [5,5,5,10,20], return true
collect $5 from the first 3 customers.
collet $10 from the fourth customer and give back $5 change.
collect $20 from the fifth customer and give back $10 change ($10 bill and $5 bill).
"""


class Solution:
    def popsicleChange(self, customers: list[int]) -> bool:
        if not customers:
            return True

        # Initialize the popsicle stand with the first customer
        popsicle_stand = {5: 0, 10: 0, 20: 0}
        if customers[0] != 5:
            return False
        popsicle_stand[customers[0]] += 1

        for customer in customers[1:]:
            if customer == 5:
                popsicle_stand[5] += 1
            elif customer == 10:
                if popsicle_stand[5] <= 0:
                    return False
                popsicle_stand[5] -= 1
                popsicle_stand[10] += 1
            elif customer == 20:
                if popsicle_stand[10] > 0 and popsicle_stand[5] > 0:
                    popsicle_stand[10] -= 1
                    popsicle_stand[5] -= 1
                elif popsicle_stand[5] >= 3:
                    popsicle_stand[5] -= 3
                else:
                    return False

        return True


# Test Cases
print(Solution().popsicleChange([5, 10]))
print(Solution().popsicleChange([10]))
print(Solution().popsicleChange([5, 5, 5, 10, 20]))
print(Solution().popsicleChange([5, 5, 10, 10, 20]))
