s = input('Введите строку:')
stack = []
flag = True
for x in s:
    if x == '(' or x == '[' or x == '{':
        stack += x
    else:
        if len(stack) != 0:
            if x == ')' and stack[-1] == '(': stack.pop()
            elif x == '}' and stack[-1] == '{' : stack.pop()
            elif x == ']' and stack[-1] == '[' : stack.pop()

            else:
                flag = False
                break

if len(stack) == 0 and flag:
    print('Строка существует')
else:
    print('Строка не существует')

