from collections import deque


class MyStack:
    def __init__(self):
        self.deque = deque()

    def push(self, x):
        self.deque.append(x)

    def pop(self):
        return self.deque.pop()

    def top(self):
        return self.deque[-1]

    def empty(self):
        return len(self.deque) == 0
