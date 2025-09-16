n = int(input("Enter a number:"))
rev = 0
num = n
while num !=0:
    div = num % 10
    rev = rev*10 + div
    num = num // 10
if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome")