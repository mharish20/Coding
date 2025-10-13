inp = input("Enter a text:").lower()
vowels = ['a','e','o','u','i']
vow = 0 
cons = 0
for i in inp:
    if i in vowels:
        vow += 1
    elif i == " ":
        pass
    else:
        cons += 1
print(f"Vowels: {vow} and Consonants: {cons}")