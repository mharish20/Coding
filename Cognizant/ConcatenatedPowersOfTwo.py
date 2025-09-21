n = int(input("Enter a number:"))
ans = ""
while n > 0:
    power = 1
    while power*2 <= n:
        power *= 2
    ans += str(power)
    n -= power
print(int(ans))
     