nums = [-1, 0, 1, 2, -1,-4]

result = []

for i in range(len(nums)):
    for j in range(len(nums[i+1:])):
        for k in range(len(nums[j+1:])):
#             print(f'i: {i}, j: {j}, k:{k}')
            if (nums[i] + nums[j] + nums[k]) == 0:
                result.append([nums[i], nums[j], nums[k]])

print(result)





# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     for i in range(len(nums)):
#         for j in range(len(nums[i+1:len(nums)])):
#               print(j)
#             if (nums[i] ==)
#
#
#     return
#
# print(threeSum(input))