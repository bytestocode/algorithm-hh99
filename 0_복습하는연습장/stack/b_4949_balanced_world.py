from sys import stdin

while True:
    string_world = stdin.readline().rstrip()
    if string_world == ".":
        break
    stack = list()

    for char in string_world:
        if char == ".":
            if not stack:
                print("yes")
                break
            else:
                print("no")
                break
        elif char == "(" or char == "[":
            stack.append(char)
            # print(f'char: {char} / stack: {stack}')
        elif char == ")":
            if not stack:
                print("no")
                break
            top = stack.pop()
            if top == "(":
                # print(f'char: {char} / stack: {stack}')
                continue
            else:
                print("no")
                break
        elif char == "]":
            if not stack:
                print("no")
                break
            top = stack.pop()
            if top == "[":
                # print(f'char: {char} / stack: {stack}')
                continue
            else:
                print("no")
                break
        else:
            continue
