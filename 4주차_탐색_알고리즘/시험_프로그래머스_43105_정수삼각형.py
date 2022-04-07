def solution(triangle):
    H = len(triangle)
    max_tri = [0] * H

    for i in range(H):
        max_tri[i] = [0] * (i + 1)

    max_tri[0][0] = triangle[0][0]

    for i in range(1, H):
        for j in range(i + 1):
            if j == 0:
                max_tri[i][j] = max_tri[i-1][j] + triangle[i][j]
            elif j == i:
                max_tri[i][j] = max_tri[i-1][j-1] + triangle[i][j]
            else:
                max_tri[i][j] = max(max_tri[i-1][j-1] + triangle[i][j], max_tri[i-1][j] + triangle[i][j])

    answer = max(max_tri[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
