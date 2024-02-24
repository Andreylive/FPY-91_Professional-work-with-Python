# Solution to check if string is balanced without OOP"

input = '((())'

stack = '('

stack = []
flag = True

for i in input:
    if i in '([{':
        stack.append(i)
    else:
        if len(stack) == 0:
            flag = False
            break
        a = stack.pop()
        if a == '(' and i == ')':
            continue
        if a == '[' and i == ']':
            continue
        if a == '{' and i == '}':
            continue
        flag = False

if flag is True and len(stack) == 0:
    print('YES')
else:
    print('NO')
