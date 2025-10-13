inp = input("Enter a string:")
res = ""
collections = set()
for i in inp:
    if i not in collections:
        collections.add(i)
        res += i
print(res)