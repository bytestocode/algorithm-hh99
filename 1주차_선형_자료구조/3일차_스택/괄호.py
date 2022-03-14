
def is_vps(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)

    print('NO' if stack else 'YES')

is_vps("(((()())()")
