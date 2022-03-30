from sys import stdin

N = int(stdin.readline())
users = []

for _ in range(N):
    age, name = stdin.readline().split()
    users.append([int(age), name])

users.sort(key=lambda user: user[0])

for user in users:
    print(user[0], user[1])
