n = 505
result = 0
while n != 0:
    num = n % 10
    result += num
    n = n // 10
print(result)