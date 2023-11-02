operators = "+-*:^"
operators_priority = {"+": 1, "-": 1, "*": 2, ":": 2, "^": 3, "(": 0}


def calculate_operation(a, b, operator):
    if operator == "-":
        return a-b
    if operator == "+":
        return a+b
    if operator == "*":
        return a*b
    if operator == ":":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        if b != 0:
            return a/b
    if operator == "^":
        return a**b


def string_is_alright(s:str) -> bool:
    s = (s.replace("-","&").replace("+","&").replace("*","&").replace(":", "&").replace("^", "&"))
    return not ("&&" in s) and not ("(&" in s) and not ("&)" in s)


def convert_to_polish_notation(s:str):
    digits_stack = ""
    stack = []
    result = []
    for i in range(len(s)):
        if s[i].isdigit():
            digits_stack += s[i]
            if i == len(s) - 1:
                result.append(digits_stack)
        if s[i] in operators:
            if len(digits_stack) != 0:
                result.append(digits_stack)
                digits_stack = ""
            while len(stack) != 0 and operators_priority[stack[-1]] >= operators_priority[s[i]]:
                result.append(stack.pop())
            stack.append(s[i])
        if s[i] == "(":
            if len(digits_stack) != 0:
                result.append(digits_stack)
                digits_stack = ""
            stack.append(s[i])
        if s[i] == ")":
            if len(digits_stack) != 0:
                result.append(digits_stack)
                digits_stack = ""
            while len(stack) != 0 and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
    while len(stack) != 0:
        result.append(stack.pop())
    return result


def calculate_from_polish_notation(converted_s: list[str]):
    result_stack = []
    for element in converted_s:
        if element.isdigit():
            result_stack.append(int(element))
        if element in operators:
            y = result_stack.pop()
            x = result_stack.pop()
            z = calculate_operation(x, y, element)
            result_stack.append(z)
    return result_stack.pop()


s = input()
if string_is_alright(s):
    print(calculate_from_polish_notation(convert_to_polish_notation(s)))