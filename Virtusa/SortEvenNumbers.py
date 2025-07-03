nums=[3,6,1,2,8,4,7,2]
even=[]
for i in range(len(nums)):
    if nums[i]%2==0:
        even.append(nums[i])
sort=sorted(even)
j=0
for i in range(len(nums)):
    if nums[i]%2==0:
        nums[i]=sort[j]
        j+=1
print(nums)