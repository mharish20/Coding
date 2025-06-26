nums=[0,2,3,0,1,5,0,2,8]
swap_point=0
for i in range(len(nums)):
    if nums[i] !=0:
        nums[swap_point]=nums[i]
        swap_point+=1
for i in range(swap_point,len(nums)):
    nums[i]=0
print(nums)