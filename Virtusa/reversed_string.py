#LIST
s=input().split()
left=0
right=len(s)-1
while right>left:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print(s)
"""
s=input("Enter your name:")
reversed=s[::-1]
print(reversed) """