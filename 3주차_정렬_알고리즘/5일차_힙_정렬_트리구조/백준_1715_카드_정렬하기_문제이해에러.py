from sys import stdin

N = int(stdin.readline())
card_mass = []

for _ in range(N):
    card_mass.append(int(stdin.readline()))

card_mass.sort()

acc = card_mass[0] * (N - 1)
for i in range(1, N):
    acc += card_mass[i] * (N - i)

print(acc)


# 해결 가능한 케이스
# N=4
# i    0  1  2  3
#     10 20 30 40
# N-i  3  3  2  1


# 해결 불가능한 케이스
#     20 25 30 35
