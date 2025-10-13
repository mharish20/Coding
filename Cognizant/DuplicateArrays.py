n = [2,5,2,5,79,5,7,3,1,7,5,6,0,23,64,2,36]
hash_map = {}
result = []
for i in n:
    hash_map[i] = hash_map.get(i,0) + 1
for key, values in hash_map.items():
    if values == 1:
        result.append(key)
print(result)