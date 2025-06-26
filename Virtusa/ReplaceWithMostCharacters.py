inp=input()
freq={}
for i in inp:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
#max_item=max(freq,key=freq.get)
most_items=max(freq.values())
changes=len(inp)-most_items
print(changes)