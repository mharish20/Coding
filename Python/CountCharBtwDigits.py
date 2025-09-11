inp = input("Enter a String:")
n = len(inp)
count = 0
for i in range(1,n-1):
    if inp[i].isalpha() and inp[i-1].isdigit() and inp[i+1].isdigit():
        count += 1
print(count)