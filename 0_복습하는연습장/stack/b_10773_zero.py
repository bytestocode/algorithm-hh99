from sys import stdin

N = int(stdin.readline())
num_list = list()

for _ in range(N):
    num = int(stdin.readline())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()

print(sum(num_list))
