from sys import stdin

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''

N, K = map(int, stdin.readline().split())
A = sorted(list(map(int, stdin.readline().split())))
B = sorted(list(map(int, stdin.readline().split())))

a_min_idx = 0
b_max_idx = N - 1
result = sum(A)

for _ in range(K):
    a_min_val = A[a_min_idx]
    b_max_val = B[b_max_idx]
    if a_min_val < b_max_val:
        result = result - a_min_val + b_max_val
        a_min_idx += 1
        b_max_idx -= 1
    else:
        break

print(result)
