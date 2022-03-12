nums = [1,4,3,2]
nums.sort()
result = 0

for i in range(int(len(nums)/2)):
    result += min(nums[i*2], nums[i*2+1])

print(result)


print(int(3.4))