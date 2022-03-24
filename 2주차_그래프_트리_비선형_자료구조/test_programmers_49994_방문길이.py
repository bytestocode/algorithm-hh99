def solution(dirs):
    answer = 0
    cur_x = 0
    cur_y = 0

    # 가본 길 저장하는 자료형
    road = list()

    for char in dirs:
        if char == "U":
            if cur_y < 5:
                cur_y += 1

                # 처음 가본 길이면 +1
                if not [[cur_x, cur_y - 1], [cur_x, cur_y]] in road:
                    road.append([[cur_x, cur_y - 1], [cur_x, cur_y]])
                    answer += 1

            else:
                continue
        elif char == "D":
            if -5 < cur_y:
                cur_y -= 1

                # 처음 가본 길이면 +1
                if not [[cur_x, cur_y], [cur_x, cur_y + 1]] in road:
                    road.append([[cur_x, cur_y], [cur_x, cur_y + 1]])
                    answer += 1

            else:
                continue
        elif char == "R":
            if cur_x < 5:
                cur_x += 1

                # 처음 가본 길이면 +1
                if not [[cur_x - 1, cur_y], [cur_x, cur_y]] in road:
                    road.append([[cur_x - 1, cur_y], [cur_x, cur_y]])
                    answer += 1

            else:
                continue
        elif char == "L":
            if -5 < cur_x:
                cur_x -= 1

                # 처음 가본 길이면 +1
                if not [[cur_x, cur_y], [cur_x + 1, cur_y]] in road:
                    road.append([[cur_x, cur_y], [cur_x + 1, cur_y]])
                    answer += 1

            else:
                continue

    return answer


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
