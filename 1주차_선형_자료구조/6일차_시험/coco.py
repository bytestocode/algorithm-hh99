import math


def solution(progresses, speeds):
    d_day_list = []

    for i in range(len(progresses)):
        # 공종별 남은 일수 계산
        d_day = math.ceil((100 - progresses[i]) / speeds[i])
        # 남은 일수 리스트 만들기
        d_day_list.append(d_day)

    answer = []
    ptr = 0
    count = 1
    max_d_day = 0
    while ptr < len(d_day_list) - 1:
        max_d_day = max(max_d_day, d_day_list[ptr])
        # 뒤에 값이 맥스보다 크면
        if max_d_day < d_day_list[ptr + 1]:
            answer.append(count)
            count = 1
            ptr += 1
        # 뒤에 값이 작으면 카운터 1 더하고 결과에 추가
        # elif d_day_list[ptr] >= d_day_list[ptr + 1]:
        else:
            count += 1
            ptr += 1
    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print('')
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
