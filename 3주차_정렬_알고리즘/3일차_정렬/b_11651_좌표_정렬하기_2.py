from sys import stdin

N = int(stdin.readline())
coordinates = []

for _ in range(N):
    x, y = stdin.readline().split()
    coordinates.append([x, y])

sorted_co = sorted(coordinates, key=lambda x: (int(x[1]), int(x[0])))


for coordinate in sorted_co:
    print(coordinate[0], coordinate[1])
