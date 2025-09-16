a = int(input())
arr1 = list(map(int,input().split()))
b = int(input())
arr2 = list(map(int,input().split()))
new_arr = []
for num in arr1:
    if num in arr2 and num not in new_arr:
        new_arr.append(num)
if new_arr:
    print(new_arr)
    print(" ".join(map(str,new_arr)))
else:
    print("No common employees")