from sys import stdin

N = int(stdin.readline())

order = 1
stack = []
answer = []

for _ in range(N):
    num = int(stdin.readline().rstrip())

    while order <= num:
        stack.append(order)
        answer.append('+')
        order += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')

if len(stack) != 0:
    print('NO')
else:
    print("\n".join([str(i) for i in answer]), end="")
