from collections import deque


def last_number(num):
    result = deque()

    # [1, 2, 3, 4, 5, 6] 리스트 만들기
    for i in range(num):
        result.append(i + 1)

    # 리스트에 하나만 남지 않은 이상
    while len(result) > 1:
        # 마지막 요소 pop
        result.popleft()
        result.append(result.popleft())

    # 마지막까지 남은 1개 요소 출력
    print(result[0])


last_number(6)