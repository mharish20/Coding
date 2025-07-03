"""nums=list(map(int,input("Enter a list of numbers:").split()))
n=len(nums)
expected=(n*(n+1))//2
actual=0
for i in nums:
    actual=actual+i
missing=expected-actual
print(missing)"""

#Sort
#268-leetcode
nums=[1,4,2,5,3,7]
sort=sorted(nums)
for i in range(1,len(nums)+1):
    if sort[i-1]!=i:
        print(i)
        