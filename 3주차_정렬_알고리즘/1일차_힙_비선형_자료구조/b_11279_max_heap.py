from sys import stdin
import heapq

N = int(stdin.readline())
max_heap = list()
answer = []

for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if len(max_heap) == 0:
            # answer.append(0)
            print(0)
            continue
        # answer.append(-heapq.heappop(max_heap))
        print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -num)

# result = ""
# for el in answer:
#     result += (str(el) + '\n')
# print(result)


# N = int(stdin.readline())
# max_heap = list()
# answer = []
# for _ in range(N):
#     num = int(stdin.readline())
#     if num == 0:
#         if len(max_heap) == 0:
#             answer.append(0)
#             continue
#         answer.append(max_heap.pop())
#     else:
#         max_heap.append(num)
#         max_heap.sort()
#
# result = ""
# for el in answer:
#     result += (str(el) + '\n')
# print(result)
