def last_number(num):
    result = []

    # [5, 4, 3, 2, 1] 리스트 만들기
    for i in range(num):
        result.insert(0, i + 1)

    # 리스트에 하나만 남지 않은 이상
    while len(result) != 1:
        # 마지막 요소 pop
        result.pop()
        # 팝했더니 하나만 남았다면 break
        if len(result) == 1:
            break
        # 둘 이상 남으면 마지막 요소를 처음으로 옮긴다
        else:
            result.insert(0, result.pop())

    # 마지막까지 남은 1개 요소 출력
    print(result[0])


last_number(5)