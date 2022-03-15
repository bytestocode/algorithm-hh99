from collections import deque


class MyStack:
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        self.deque.append(value)

    def peek(self):
        return self.deque[0]

    def pop(self):
        return self.deque.popleft()

    def empty(self):
        return len(deque) == 0
