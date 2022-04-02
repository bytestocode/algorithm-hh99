from sys import stdin

N, M = list(map(int, stdin.readline().split()))
tree_list = list(map(int, stdin.readline().split()))

start = 0
end = max(tree_list)

h = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in tree_list:
        if tree > mid:
            total += tree - mid
    if total < M:
        end = mid - 1
    else:
        h = mid
        start = mid + 1

print(h)
