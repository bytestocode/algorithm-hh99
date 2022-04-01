from sys import stdin

N = int(stdin.readline())
N_list = list(map(int, stdin.readline().split()))

M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

N_list.sort()

for target in M_list:
    start = 0
    end = N - 1
    res = 0

    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] > target:
            end = mid - 1
        elif N_list[mid] < target:
            start = mid + 1
        else:
            res = 1
            break

    print(res, end=' ')
