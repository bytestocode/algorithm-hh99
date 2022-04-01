def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while not l == r:
        if numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            return [l + 1, r + 1]
