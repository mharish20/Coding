inp = input("Enter a text:").lower()
vowels = ['a','e','o','u','i']
count = 0 
for i in inp:
    if i in vowels:
        count += 1
print(count)