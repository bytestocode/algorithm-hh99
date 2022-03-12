s = "babad"


def longestPalindrome(self, s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print(longestPalindrome(s))

# 오답 bb 같이 앞뒤가 같은 경우 판단을 못함
# for i in range(len(s)):
#     for j in range(i+1):
#         palin = s[j:len(s)-i-j]
#         if palin == palin[::-1]:
#             print(palin)
