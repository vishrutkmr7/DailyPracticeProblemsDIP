"""
This question is asked by Apple.
You are serving people in a lunch line and need to ensure each person gets a “balanced” meal.
A balanced meal is a meal where there exists the same number of food items as drink items.
Someone is helping you prepare the meals and hands you food items (i.e. F) or a drink items (D)
in the order specified by the items string. Return the maximum number of balanced meals you
are able to create without being able to modify items.
Note: items will only contain F and D characters.

Ex: Given the following items…

items = "FDFDFD", return 3
the first "FD" creates the first balanced meal.
the second "FD" creates the second balanced meal.
the third "FD" creates the third balanced meal.
Ex: Given the following items…

items = "FDFFDFDD", return 2
"FD" creates the first balanced meal.
"FFDFDD" creates the second balanced meal.
"""


from inspect import stack


class Solution:
    def balancedMeals(self, items: str) -> int:
        # Check if substrings in items are balanced
        foodCounter = 0
        drinkCounter = 0
        mealsCounter = 0
        for item in items:
            if item == "F":
                foodCounter += 1
            else:
                drinkCounter += 1

            if foodCounter == drinkCounter:
                mealsCounter += 1

        return mealsCounter


# Test Cases
print(Solution().balancedMeals("FDFDFD"))
print(Solution().balancedMeals("FDFFDFDD"))
print(Solution().balancedMeals(""))
