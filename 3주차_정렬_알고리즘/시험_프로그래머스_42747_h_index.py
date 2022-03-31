def solution(citations):
    answer = 0

    sorted_citations = sorted(citations)

    for i in range(len(sorted_citations)):
        h = len(sorted_citations) - i
        if sorted_citations[i] >= h:
            answer = h
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
