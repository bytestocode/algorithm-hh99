from sys import stdin

M, N = map(int, stdin.readline().split())
chess_layout = []
total_count = 32

for i in range(M):
    chess_layout.append(stdin.readline().rstrip())

# print(chess_layout)


def count_repaint(row_start, col_start):
    count = 0
    # print(f'row_start: {row_start}')
    # print(f'col_start: {col_start}')
    for row in range(row_start, row_start + 8):
        for col in range(col_start, col_start + 8):
            if row % 2 == 0 and col % 2 == 0:
                if chess_layout[row][col] != "W":
                    count += 1
            elif row % 2 == 0 and col % 2 != 0:
                if chess_layout[row][col] != "B":
                    count += 1
            elif row % 2 != 0 and col % 2 == 0:
                if chess_layout[row][col] != "B":
                    count += 1
            else:
                if chess_layout[row][col] != "W":
                    count += 1

    return min(count, 64 - count)


for i in range(M - 8 + 1):
    for j in range(N - 8 + 1):
        total_count = min(total_count, count_repaint(i, j))

print(total_count)
