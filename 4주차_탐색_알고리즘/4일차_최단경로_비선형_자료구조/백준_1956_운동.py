import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = int(1e9)
dist = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

result = INF
for i in range(V+1):
    result = min(result, dist[i][i])
if result == INF:
    print(-1)
else:
    print(result)


'''
3 4
1 2 1
3 2 1
1 3 5
2 3 2
'''
