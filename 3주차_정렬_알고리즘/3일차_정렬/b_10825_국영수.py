from sys import stdin

N = int(stdin.readline())
students = []

for _ in range(N):
    name, kor, eng, math = stdin.readline().split()
    student = {
        'name': name,
        'kor': int(kor),
        'eng': int(eng),
        'math': int(math),
    }
    students.append(student)

sorted_dict = sorted(students, key=lambda x: x['name'])
sorted_math = sorted(sorted_dict, key=lambda x: x['math'], reverse=True)
sorted_eng = sorted(sorted_math, key=lambda x: x['eng'])
sorted_kor = sorted(sorted_eng, key=lambda x: x['kor'], reverse=True)

for student in sorted_kor:
    print(student['name'])
