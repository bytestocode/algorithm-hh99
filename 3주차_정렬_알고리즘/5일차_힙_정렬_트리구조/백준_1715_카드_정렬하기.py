from sys import stdin
import heapq

N = int(stdin.readline())
card_mass = []

for _ in range(N):
    heapq.heappush(card_mass, int(stdin.readline()))

acc = 0
while card_mass:
    if len(card_mass) == 1:
        break

    min1 = heapq.heappop(card_mass)
    min2 = heapq.heappop(card_mass)
    sum = min1 + min2
    acc += sum
    heapq.heappush(card_mass, sum)

print(acc)
