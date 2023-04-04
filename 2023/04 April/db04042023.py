"""
Given the hours and the minutes on an analog clock, return the angle formed between the two hands.
Note: Return the smaller of the two angles formed.

Ex: Given the following hours and minutes...

hours = 12, minutes = 0, return 0 (the hands are on top of each other).
Ex: Given the following hours and minutes...

hours = 3, minutes = 25, return 47.5.
"""


class Solution:
    def angleClock(self, hours: int, minutes: int) -> float:
        hour_angle = (hours % 12 + minutes / 60) * 30
        minute_angle = minutes * 6
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360 - angle)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.angleClock(12, 0))
    print(solution.angleClock(3, 25))
