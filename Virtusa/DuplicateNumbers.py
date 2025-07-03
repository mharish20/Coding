#leetcode 287
nums=[2,4,6,3,2,5,0]
slow=nums[0]
fast=nums[0]
while True:
    slow=nums[slow]
    fast=nums[nums[fast]]
    if slow==fast:
        break

slow=nums[0]
while slow!=fast:
    slow=nums[slow]
    fast=nums[fast]

print(f"Duplicate number is:{slow}")

"""
nums=[2,4,6,3,2,5,0]
sort=sorted(nums)
for i in range(len(sort)-1):
    if sort[i]==sort[i+1]:
        print(sort[i])
"""