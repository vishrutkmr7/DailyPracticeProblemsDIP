"""
This question is asked by Amazon.
Given N distinct rooms that are locked we want to know if you can unlock and visit every room.
Each room has a list of keys in it that allows you to unlock and visit other rooms.
We start with room 0 being unlocked. Return whether or not we can visit every room.
 
Ex: Given the following rooms…

rooms = [[1], [2], []], return true
Ex: Given the following rooms…

rooms = [[1, 2], [2], [0], []], return false, we can’t enter room 3.
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                stack.extend(rooms[room])
        return len(visited) == len(rooms)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.canVisitAllRooms([[1], [2], []]) == True
    assert solution.canVisitAllRooms([[1, 2], [2], [0], []]) == False
    print("All tests passed.")
