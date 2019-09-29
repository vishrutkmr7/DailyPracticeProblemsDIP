# This problem was recently asked by Microsoft:

# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.


def calcAngle(h, m):
    # Fill this in.
    ans = abs((h * 30 + m * 0.5) - (m * 6))
    return int(min(360 - ans, ans))


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
