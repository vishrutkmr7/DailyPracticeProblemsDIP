# This problem was recently asked by Twitter:

# Implement a class for a stack that supports all the regular functions (push, pop) and
# an additional function of max() which returns the maximum element in the stack (return None if the stack is empty)
# Each method should run in constant time.

class MaxStack:
    def __init__(self):
        # Fill this in.
        self.items = []
  
    def push(self, val):
        # Fill this in.
        self.items.append(val)
  
    def pop(self):
        # Fill this in.
        return self.items.pop()
  
    def max(self):
        # Fill this in.
        maxN = 0
        if len(self.items) == 0:
            return None

        for i in self.items:
            if i >= maxN:
                maxN = i
        
        return maxN
  
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (s.max())
# 3
s.pop()
s.pop()
print (s.max())
# 2