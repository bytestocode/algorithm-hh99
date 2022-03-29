def solution(N, stages):
    answer = []
    cnt_fail = {}
    for i in range(N+1):
        cnt_fail[i+1] = 0

    fail_ratio = {}

    sorted_stages = sorted(stages)

    for stage in sorted_stages:
        cnt_fail[stage] += 1

    acc = 0
    for key, val in cnt_fail.items():
        if key <= N and len(stages) > acc:
            print(f'key: {val}')
            print(f'분모: {(len(stages) - acc)}')
            fail_ratio[key] = val / (len(stages) - acc)
        else:
            fail_ratio[key] = 0
        acc += val

    result = sorted(fail_ratio.items(), key=lambda x: -x[1])

    for item in result:
        answer.append(item[0])

    return answer[:-1]