from sys import stdin

N = int(stdin.readline())
word_list = []

for _ in range(N):
    char = stdin.readline().rstrip()
    word_list.append(char)

sorted_list = sorted(sorted(word_list), key=lambda x: len(x))

result = []
for value in sorted_list:
    if value not in result:
        result.append(value)

for val in result:
    print(val)
