n = [2,4,5,2,1,2,4,6,8,3,5,7,8,4,6]
hash_map = {}
res = []
for i in n:
    hash_map[i] = hash_map.get(i,0)+1
for key,values in hash_map.items():
    res.append(key)
print(res)