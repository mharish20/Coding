def reverse(start,end):
    nums[start],nums[end]=nums[end],nums[start]
    start+=1
    end-=1

nums=[1,2,3,4,5,6,7,8]
n=len(nums)
k=int(input("Enter the number of times to rotate:"))
first=reverse(0,n-1)
print(first)
