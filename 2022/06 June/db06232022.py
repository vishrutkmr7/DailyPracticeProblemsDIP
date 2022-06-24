"""
Design a class to implement a stack using only a single queue.
Your class, QueueStack, should support the following stack methods:
push() (adding an item), pop() (removing an item), peek() (returning the top value without removing it),
and empty() (whether or not the stack is empty).
"""


class QueueStack:
    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        while self.queue:
            self.stack.append(self.queue.pop(0))
        return self.stack.pop()

    def peek(self):
        while self.queue:
            self.stack.append(self.queue.pop(0))
        return self.stack[-1]

    def empty(self):
        return not self.stack and not self.queue

# Test
qs = QueueStack()
qs.push(1)
qs.push(2)
qs.push(3)
print(qs.pop())
print(qs.pop())
print(qs.pop())
print(qs.empty())
qs.push(4)
print(qs.peek())
print(qs.empty())
