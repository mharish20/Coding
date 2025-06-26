st="a3b2c1"
final=''
for i in range(0,len(st),2):
    char=st[i]
    count=int(st[i+1])
    final +=char*count
print(final)