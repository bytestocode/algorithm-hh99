class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # 아웃풋이 없으면 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        # return 값이 필요한 이유?
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []
