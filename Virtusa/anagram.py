#Silent --> Listen 
#File --> Life
f="harish"
s="shari"
if len(s)!=len(f):
    print("False")
f_hash={}
s_hash={}
for char in f:
    f_hash[char]=f_hash.get(char,0)+1
for char in s:
    s_hash[char]=s_hash.get(char,0)+1
print(f_hash==s_hash)