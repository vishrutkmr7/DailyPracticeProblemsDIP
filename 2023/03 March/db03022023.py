"""
You are going on a vacation in which you need to take multiple planes to get to your destination.
You are given a list, flights, that represents a set of your flights. Each flight is a list itself that
contains two elements, the departing city and the arriving city respectively. Return the destination city.
Note: The destination city is the city that does not contain an outgoing flight and it is guaranteed there
is a unique answer. 

Ex: Given the following flights…

flights = [["A", "B"], ["B", "C"]], return "C".
Ex: Given the following flights…

flights = [["A", "B"], ["C", "D"], ["B", "C"]], return "D".
"""


class Solution:
    def destCity(self, flights: list[list[str]]) -> str:
        cities = {flight[0] for flight in flights}
        for flight in flights:
            if flight[1] not in cities:
                return flight[1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.destCity([["A", "B"], ["B", "C"]]))
    print(solution.destCity([["A", "B"], ["C", "D"], ["B", "C"]]))
