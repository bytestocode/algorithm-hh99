from sys import stdin

N = int(stdin.readline())
house = list(map(int, stdin.readline().split()))
sorted_house = sorted(house)
print(sorted_house)

mid = N // 2 - 1 if N % 2 == 0 else N // 2

print(sorted_house[mid])
