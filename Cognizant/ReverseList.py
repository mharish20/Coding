n = [1,2,3,4,5,6,7,8]
start = 0 
end = len(n) - 1
while start <= end:
    n[start],n[end]=n[end],n[start]
    start += 1
    end -= 1
print(n)