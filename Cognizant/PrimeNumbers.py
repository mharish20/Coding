num = int(input("Enter a number:"))
if num < 2:
    print(f"{num} is not a Prime")
    exit()
for i in range(2,int(num ** 0.5)+1):
    if num % i == 0:
        print(f"{num} is a not Prime")
        exit()
print(f"{num} is a Prime")