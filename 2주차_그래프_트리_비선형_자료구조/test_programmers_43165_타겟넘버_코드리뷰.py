def solution(numbers, target):
    answer = 0

    # 깊이우선탐색으로 합계를 하나씩 계산
    # 매개변수: 몇번째 숫자인지?, 현재까지 합계는? 2가지 대입
    def dfs(idx, cur_sum):
        # 인덱스가 주어진 숫자와 같아지면 dfs 종료
        # target과 같으면 answer +1
        if idx == len(numbers):
            if cur_sum == target:
                nonlocal answer
                answer += 1
                return
            else:
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

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
