from sys import stdin

N = int(stdin.readline())
card_mass = []

for _ in range(N):
    card_mass.append(int(stdin.readline()))

card_mass.sort()

if N == 1:
    acc = card_mass[0]

else:
    acc = card_mass[0] * (N - 1)
    for i in range(1, N):
        acc += card_mass[i] * (N - i)

print(acc)
