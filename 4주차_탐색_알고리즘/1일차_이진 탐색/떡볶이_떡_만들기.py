from sys import stdin

N, M = list(map(int, stdin.readline().split()))
tteok_list = list(map(int, stdin.readline().split()))

tteok_list.sort(reverse=True)

sum = 0
h = tteok_list[0]
while sum < M:
    for i in range(N):
        if tteok_list[i] - h > 0:
            sum += (tteok_list[i] - h)
        else:
            h -= 1
            break

print(h)


'''
4 6
19 15 10 17
'''
