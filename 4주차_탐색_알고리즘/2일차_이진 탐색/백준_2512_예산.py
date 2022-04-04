from sys import stdin

N = int(stdin.readline())
budget_list = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
max_budget = max(budget_list)

if sum(budget_list) <= M:
    print(max_budget)

start = 1
end = max_budget

while start <= end:
    print(start, end)
    total = 0
    mid = (start + end) // 2

    for budget in budget_list:
        if budget > mid:
            total += mid
        else:
            total += budget

    print(total, start, end)
    # 처음 조건식 => if total < M:
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1
    print(total, start, end)

print(end)
