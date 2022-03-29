def solution(N, stages):
    answer = []
    total_users = len(stages)

    # 스테이지별 도전자 숫자 카운트
    challenge_user_count = {}
    for stage in range(1, N + 2):
        challenge_user_count[stage] = 0

    for stage in stages:
        challenge_user_count[stage] += 1

    print(challenge_user_count)
    # => {1: 1, 2: 3, 3: 2, 4: 1, 5: 0, 6: 1}

    # 스테이지별 실패율 계산
    stage_fails = {}

    acc_users = 0
    for stage, users in challenge_user_count.items():
        if stage <= N and acc_users < total_users:
            stage_fails[stage] = users / (total_users - acc_users)
        else:
            stage_fails[stage] = 0
        acc_users += users

    print(stage_fails)
    # => {1: 0.125, 2: 0.42..., 3: 0.5, 4: 0.5, 5: 0.0, 6: 0}

    # 실패율 큰 순으로 정렬
    sorted_stage_fails = sorted(stage_fails.items(), key=lambda x: -x[1])
    for stage in sorted_stage_fails:
        answer.append(stage[0])

    # N+1 제외하고 출력
    return answer[:-1]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
