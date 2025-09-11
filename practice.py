#Right triangle
"""n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print('* ' * i )"""

#Triangle
n = int(input("Enter the number of rows:"))
for i in range(n):
    print(" "*(n-i-1) + "* " * (i+1))