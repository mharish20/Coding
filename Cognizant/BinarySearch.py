n = [1,2,3,4,5,6,7,8,9,10]
target = int(input("Enter a number to find:"))
start = 0
end = len(n) - 1
while start <= end:
    mid = (start+end)//2
    if n[mid] == target:
        print(mid)
        exit()
    elif n[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
print(mid)