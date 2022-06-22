"""
This question is asked by Microsoft. Design a class, MovingAverage,
which contains a method, next that is responsible for returning the moving average
from a stream of integers. 
Note: a moving average is the average of a subset of data at a given point in time. 

Ex: Given the following series of events...

// i.e. the moving average has a capacity of 3.
MovingAverage movingAverage = new MovingAverage(3);
m.next(3) returns 3 because (3 / 1) = 3
m.next(5) returns 4 because (3 + 5) / 2 = 4 
m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6
"""


class MovingAverage:
    def __init__(self, capacity) -> None:
        self.queue = []
        self.capacity = capacity

    def next(self, x: int) -> int:
        """Implement a queue Data structure"""
        self.queue.append(x)
        if len(self.queue) > self.capacity:
            self.queue.pop(0)
        return sum(self.queue) // len(self.queue)


# Test
m = MovingAverage(3)
print(m.next(3))
print(m.next(5))
print(m.next(7))
print(m.next(6))
print(m.next(8))
