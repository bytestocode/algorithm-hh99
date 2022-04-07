def solution(n, times):
    answer = 0
    avg = n // len(times)

    start = 1
    end = avg * max(times)

    while start <= end:
        mid = (start + end) // 2

        sum = 0
        for i in range(len(times)):
            sum += mid // times[i]

        if sum >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(6, [7, 10]))
