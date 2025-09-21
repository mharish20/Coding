n = int(input("Enter a number:"))
a,b = 0,1
fibonacci = []
for i in range(n):
    fibonacci.append(a)
    a , b = b, a+b
print(fibonacci)