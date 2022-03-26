from sys import stdin
import heapq

N = int(stdin.readline())
abs_heap = []
x_count_dict = {}

for _ in range(N):
    val_x = int(stdin.readline())

    if val_x == 0:
        if len(abs_heap) == 0:
            print(0)
            continue

        # 절댓값이 가장 작은값 삭제하면서 변수에 추가
        abs_min = heapq.heappop(abs_heap)
        # 음수 키가 dict에 있으면
        if -abs_min in x_count_dict:
            # 음수 값이 0보다 크면 음수로 출력하고 음수 개수 -1
            if x_count_dict[-abs_min] > 0:
                print(-abs_min)
                x_count_dict[-abs_min] -= 1
                continue

        print(abs_min)

    # x값을 키로 하는 사전 자료형을 만들고, heap에는 절댓값으로 추가
    else:
        if val_x not in x_count_dict:
            x_count_dict[val_x] = 1
        else:
            x_count_dict[val_x] += 1
        heapq.heappush(abs_heap, abs(val_x))
