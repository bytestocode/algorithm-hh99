import re


def split_name(name):
    head = ''
    number = ''
    tail = ''
    for i in range(len(name)):
        if head == '' and re.match(r'[\d]', name[i]):
            head = name[:i]
        elif head != '' and re.match(r'[\D]', name[i]):
            number = name[len(head):i]
            tail = name[i:]
            break
        # elif i == len(name) - 1:
        if i == len(name) - 1:
            number = name[len(head):]
            tail = ''

    return [head, number, tail]


def solution(files):
    answer = []

    for file in files:
        answer.append(split_name(file))
        # answer.sort(key=lambda name: (name[0].lower(), int(name[1].lstrip('0'))))
        answer.sort(key=lambda name: (name[0].lower(), int(name[1])))

    for i in range(len(answer)):
        answer[i] = answer[i][0] + answer[i][1] + answer[i][2]

    return answer


print(solution(["img00000000", "img1.png", "img2", "IMG02"]))
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "F-15"]))
