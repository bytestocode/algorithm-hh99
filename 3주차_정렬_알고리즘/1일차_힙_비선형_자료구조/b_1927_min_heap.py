from sys import stdin
import heapq

N = int(stdin.readline())
min_heap = list()
answer = []

for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if len(min_heap) == 0:
            answer.append(0)
            # print(0)
            continue
        answer.append(heapq.heappop(min_heap))
        # print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, num)

# result = ""
# for el in answer:
#     result += (str(el) + '\n')
# print(result)

print("\n".join([str(i) for i in answer]), end="")
