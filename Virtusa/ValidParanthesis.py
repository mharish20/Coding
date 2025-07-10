s="(({}))"
stack=[]
pair={
    ')' : '(',
    ']' : '[',
    '}' : '{'
}
for ch in s:
    if ch in pair.values():
        stack.append(ch)
    else:
        if not stack or stack[-1]!=pair[ch]:
            print("False")
            exit()
        stack.pop()
print(not stack)
    