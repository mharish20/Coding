# Search an element in a sorted array with time complexity of logn
# Move zeros to the end of the array
inp = [1,2,4,5,6,7,8,9]
target=int(input("Enter the number to search:"))
min = 0
maxi = len(inp)-1
while min <= maxi:
    mid = (min+maxi)//2
    if inp[mid] == target:
        print(mid)
        exit()
    elif inp[mid] < target:
        min = mid + 1
    else:
        maxi = mid - 1
print(mid)
        