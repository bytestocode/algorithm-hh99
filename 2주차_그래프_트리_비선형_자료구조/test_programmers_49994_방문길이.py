def solution(dirs):
    answer = 0

    # 현재 좌표 저장
    cur_x = 0
    cur_y = 0

    # 리스트 생성: 방문한 경로 저장
    visited_path = list()

    for char in dirs:
        if char == "U":
            # 현재 y 좌표가 5 미만? Up 가능!
            if cur_y < 5:
                cur_y += 1
                # 처음 가본 길이면 +1
                if not [[cur_x, cur_y - 1], [cur_x, cur_y]] in visited_path:
                    visited_path.append([[cur_x, cur_y - 1], [cur_x, cur_y]])
                    answer += 1
            else:
                continue

        elif char == "D":
            # 현재 y 좌표가 -5 초과? Down 가능!
            if -5 < cur_y:
                cur_y -= 1
                # 처음 가본 길이면 +1
                if not [[cur_x, cur_y], [cur_x, cur_y + 1]] in visited_path:
                    visited_path.append([[cur_x, cur_y], [cur_x, cur_y + 1]])
                    answer += 1
            else:
                continue

        elif char == "R":
            # 현재 x 좌표가 5 미만? Right 가능!
            if cur_x < 5:
                cur_x += 1
                # 처음 가본 길이면 +1
                if not [[cur_x - 1, cur_y], [cur_x, cur_y]] in visited_path:
                    visited_path.append([[cur_x - 1, cur_y], [cur_x, cur_y]])
                    answer += 1
            else:
                continue

        elif char == "L":
            # 현재 x 좌표가 -5 초과? Left 가능!
            if -5 < cur_x:
                cur_x -= 1
                # 처음 가본 길이면 +1
                if not [[cur_x, cur_y], [cur_x + 1, cur_y]] in visited_path:
                    visited_path.append([[cur_x, cur_y], [cur_x + 1, cur_y]])
                    answer += 1
            else:
                continue

    return answer


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
