from sys import stdin

N = int(stdin.readline())

stack = list()
answer = []

for _ in range(N):
    command = stdin.readline().split()

    if command[0] == 'push':
        val = int(command[1])
        stack.append(val)
    elif command[0] == 'pop':
        answer.append(stack.pop() if len(stack) != 0 else -1)
    elif command[0] == 'size':
        answer.append(len(stack))
    elif command[0] == 'empty':
        answer.append(0 if len(stack) != 0 else 1)
    elif command[0] == 'top':
        answer.append(stack[-1] if len(stack) != 0 else -1)

result = ""
for el in answer:
    result += (str(el) + '\n')
print(result)
