lists = []
input1 = int(input())
input2 = list(map(int,input().split()))
i = 0
count = 0
while i < input1:
    while lists and input2[i] >= lists[-1]:
        lists.pop()
        count += 1
    lists.append(input2[i])
    i += 1
print(count)