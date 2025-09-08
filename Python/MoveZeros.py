nums = [0,2,4,7,2,0,3,6,8,0,1,2,4,0,0,2,3]
swap_point = 0
n = len(nums)
for i in range(n):
    if nums[i] != 0:
        nums[swap_point] = nums[i]
        swap_point += 1
for i in range(swap_point,n):
    nums[i] = 0
print(nums)