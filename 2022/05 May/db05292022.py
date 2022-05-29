"""
This question is asked by Amazon.
Given a string representing the sequence of moves a robot vacuum makes,
return whether or not it will return to its original position.
The string will only contain L, R, U, and D characters, representing left, right, up,
and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""


def robot_vacuum(moves):
    """
    The robot starts at the origin (0, 0) and faces up.
    The robot can move up, down, left or right,
    but cannot move diagonally or face a different direction.
    """
    x, y = 0, 0
    for move in moves:
        if move == "L":
            y += 1
        elif move == "R":
            y -= 1
        elif move == "U":
            x += 1
        elif move == "D":
            x -= 1
    return x == 0 and y == 0


# Test cases
print(robot_vacuum("LR"))
print(robot_vacuum("URURD"))
print(robot_vacuum("RUULLDRD"))
