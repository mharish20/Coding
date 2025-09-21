arr = [3,5,2,13,65,13,52,89]
target = int(input("Enter a number to search:"))
for i in range(len(arr)):
    if arr[i] == target:
        print(f"{target} is found at the index {i}")
        exit()
else:
    print(f"{target} is not found in the array")