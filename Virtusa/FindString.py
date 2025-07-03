text=input()
string=input()
n=len(string)
for i in range(len(text)):
    if text[i:i+n]==string:
        print(i)
