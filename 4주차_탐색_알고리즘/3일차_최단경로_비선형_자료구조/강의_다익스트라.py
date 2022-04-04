import sys

input = sys.stdin.readline
INF = int(1e9)

with open('testcase1.txt') as f:
    sys.stdin = f
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))


def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    visited = [False] * N
    dist = [INF] * N

    visited[start] = True
    dist[start] = 0

    for adj, d in graph[start]:
        dist[adj] = d

    # N개의 노드 중 첫 노드는 이미 방문했으므로,
    # N-1번 수행하면 된다.
    for _ in range(N - 1):
        # 가장 가깝고 방문 안한 녀석을 고르고,
        cur = get_smallest_node()
        visited[cur] = True
        # 최단거리를 비교, 수정한다.
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost

    return dist


assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
