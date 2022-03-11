import string


def count_word(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(" ".join(str(num) for num in result))


count_word("baekjoon")
