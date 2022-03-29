
def sort_colors(nums):
    red, white, blue = 0, 0, len(nums)

    while white < blue:
        if nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        elif nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        else:
            white += 1


