from collections import deque
from sys import stdin

N = int(stdin.readline())

queue = deque()
answer = []


for _ in range(N):
    command = stdin.readline().split()

    if command[0] == 'push':
        val = int(command[1])
        queue.append(val)
    elif command[0] == 'pop':
        answer.append(queue.popleft() if len(queue) != 0 else -1)
    elif command[0] == 'size':
        answer.append(len(queue))
    elif command[0] == 'empty':
        answer.append(0 if len(queue) != 0 else 1)
    elif command[0] == 'front':
        answer.append(queue[0] if len(queue) != 0 else -1)
    elif command[0] == 'back':
        answer.append(queue[-1] if len(queue) != 0 else -1)

result = ""
for el in answer:
    result += (str(el) + '\n')
print(result)
