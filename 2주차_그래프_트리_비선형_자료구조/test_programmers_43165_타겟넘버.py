def solution(numbers, target):
    answer = 0

    # 리스트 생성: 합계를 하나씩 계산해서 저장
    sum_list = list()

    # 깊이우선탐색으로 합계를 하나씩 계산
    # 매개변수: 몇번째 숫자인지?, 현재까지 합계는? 2가지 대입
    def dfs(idx, cur_sum):
        # 인덱스가 주어진 숫자와 같아지면 합계를 구한 것
        # 합계 리스트에 추가하고 dfs 종료
        if idx == len(numbers):
            sum_list.append(cur_sum)
            return

        # 인덱스에 해당하는 숫자를 더하는 dfs
        sum_plus = cur_sum + numbers[idx]
        # 다음번 인덱스로 넘어감
        dfs(idx + 1, sum_plus)

        # 인덱스에 해당하는 숫자를 빼는 dfs
        sum_minus = cur_sum - numbers[idx]
        # 다음번 인덱스로 넘어감
        dfs(idx + 1, sum_minus)

    # 인덱스 0, 합계 0부터 dfs 시작
    dfs(0, 0)

    # 합계 리스트에 4가 있으면 answer +1
    for i in range(len(sum_list)):
        if sum_list[i] == target:
            answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1]	, 4))
