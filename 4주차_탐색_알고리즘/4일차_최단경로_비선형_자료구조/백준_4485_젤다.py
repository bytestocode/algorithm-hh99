import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cur, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N:
                acc = cur + graph[next_x][next_y]

                if acc < distance[next_x][next_y]:
                    distance[next_x][next_y] = acc
                    heapq.heappush(q, (acc, next_x, next_y))


N = int(input())
count = 1
while N != 0:
    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    dijkstra()

    N = int(input())
    count += 1

# count = 1
#
# while True:
#     N = int(input())
#     if N == 0:
#         break
#
#     graph = [list(map(int, input().split()) for _ in range(N))]
#     distance = [[INF] * N for _ in range(N)]
#
#     dijkstra(graph, distance, count)
#     count += 1

