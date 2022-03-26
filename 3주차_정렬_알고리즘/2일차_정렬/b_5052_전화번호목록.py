from sys import stdin

answer = []

t = int(stdin.readline())
for _ in range(t):

    result = "YES"

    n = int(stdin.readline())
    phone_nums = []
    for _ in range(n):
        phone_nums.append(stdin.readline().rstrip())

    sorted_nums = sorted(phone_nums)

    # for문을 1번으로 줄임
    for i in range(n - 1):
        cur_num = sorted_nums[i]
        next_num = sorted_nums[i + 1]
        if cur_num == next_num[:len(cur_num)]:
            result = "NO"
            break

    answer.append(result)

print("\n".join([str(i) for i in answer]), end="")
