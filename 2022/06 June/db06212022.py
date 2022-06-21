"""
This question is asked by Google.
Create a class CallCounter that tracks the number of calls a client has made within the last 3 seconds.
Your class should contain one method, ping(int t) that receives the current timestamp (in milliseconds)
of a new call being made and returns the number of calls made within the last 3 seconds.
Note: you may assume that the time associated with each subsequent call to ping is strictly increasing.

Ex: Given the following calls to ping…

ping(1), return 1 (1 call within the last 3 seconds)
ping(300), return 2 (2 calls within the last 3 seconds)
ping(3000), return 3 (3 calls within the last 3 seconds)
ping(3002), return 3 (3 calls within the last 3 seconds)
ping(7000), return 1 (1 call within the last 3 seconds)
"""


class CallCounter:
    def __init__(self) -> None:
        self.last_call = 0
        self.count = 0

    def ping(self, t: int) -> int:
        if t - self.last_call > 3000:
            self.count = 0
        self.last_call = t
        self.count += 1
        return self.count


# Test
counter = CallCounter()
print(counter.ping(1))
print(counter.ping(300))
print(counter.ping(3000))
print(counter.ping(3002))
print(counter.ping(7000))
print(counter.ping(8000))
print(counter.ping(8001))
print(counter.ping(8002))
