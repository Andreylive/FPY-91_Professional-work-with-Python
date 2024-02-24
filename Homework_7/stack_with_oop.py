from class_stack import Stack
# Solution to check if string is balanced using OOP"


def check_balance(input: str) -> str:
    """ Function to check if sting is balanced"""
    flag = True
    stack_object = Stack()

    for i in input:
        if i in '([{':
            stack_object.push(i)
        else:
            len_stack = stack_object.size()
            if len_stack == 0:
                return 'Несбалансированно'
            last_element = stack_object.pop()

            if last_element == '(' and i == ')':
                continue
            if last_element == '[' and i == ']':
                continue
            if last_element == '{' and i == '}':
                continue
            flag = False

    if flag is True and stack_object.size() == 0:
        return 'Сбалансировано'
    return 'Несбалансировано'


check_balance = check_balance('((())')
print(check_balance)
