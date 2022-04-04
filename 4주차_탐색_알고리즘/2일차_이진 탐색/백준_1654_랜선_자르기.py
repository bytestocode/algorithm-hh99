from sys import stdin

K, N = list(map(int, stdin.readline().split()))
lan_list = [int(stdin.readline()) for _ in range(K)]

start = 1
end = max(lan_list)

while start <= end:
    mid = (start+end) // 2
    lan_sum = 0

    for lan in lan_list:
        lan_sum += lan // mid

    if lan_sum >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
