import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [INF] * (V + 1)

q = []
heapq.heappush(q, (0, K))
dist[K] = 0

while q:
    acc, cur = heapq.heappop(q)

    if dist[cur] < acc:
        continue

    for adj, d in graph[cur]:
        cost = acc + d
        if cost < dist[adj]:
            dist[adj] = cost
            heapq.heappush(q, (cost, adj))

for i in range(1, V + 1):
    if dist[i] != INF:
        print(dist[i])
    else:
        print("INF")

'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
