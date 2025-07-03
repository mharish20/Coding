nums=[2,1,1,1,2,2,2]
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq.items())
for key,values in freq.items():
    if values>(len(nums))//2:
        print("Most repeated number that is more than the half length of array:",key)
        break