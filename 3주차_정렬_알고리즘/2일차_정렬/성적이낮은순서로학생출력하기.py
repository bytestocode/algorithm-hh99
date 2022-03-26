from sys import stdin

'''
5
홍길동 95
이순신 77
파이썬 99
호랑이 99
파이썬 78
'''

N = int(stdin.readline())
students = []

for _ in range(N):
    name, score = stdin.readline().split()
    student = {'name': name, 'score': int(score)}
    students.append(student)
# 완성된 배열: [[95, 홍길동], [77, 이순신], [99, 파이썬], [99, 호랑이], [78, 파이썬]]

sorted_students = sorted(students, key=lambda x: x['score'])
# 정렬된 배열: [[77, 이순신], [78, 파이썬], [95, 홍길동], [99, 파이썬], [99, 호랑이]]

for student in sorted_students:
    print(student['name'], end=' ')
# 학생 객체(dict)의 이름 출력: 이순신 파이썬 홍길동 파이썬 호랑이
