from sys import stdin

N = int(stdin.readline())
n_list = stdin.readline().split()

M = int(stdin.readline())
m_list = stdin.readline().split()

n_list.sort()
m_list.sort()

i = 0
j = 0
while i < M:
    if m_list[i] == n_list[j]:
        print('yes', end=' ')
        i += 1
        j += 1
    elif m_list[i] > n_list[j]:
        j += 1
    else:
        print('no', end=' ')
        i += 1


'''
5
8 3 7 9 2
3
5 7 9
'''