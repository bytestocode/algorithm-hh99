input = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemperatures(temperatures):
    result = []

    for i in range(len(temperatures)):
        is_added = False
        for j in range(i + 1, len(temperatures)):
            if temperatures[i] < temperatures[j]:
                result.append(j - i)
                is_added = True
                break
        if not is_added:
            result.append(0)

    return result


print(dailyTemperatures(input))
