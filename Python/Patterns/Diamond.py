n = int(input("Enter a number:"))       
for i in range(n):
    print(" "*(n-i-1)+ "* "*(i+1))
    print()
for j in range(n,0,-1):
    print(" "*(n-j+1) + "* "*(j-1))
    print()