def evaluate_postfix(postfix_list):
    container=Stack()
    for i in range(len(postfix_list)):
        if postfix_list[i].isdigit():
            container.push(int(postfix_list[i]))
        else:
            numbers2=container.pop()
            numbers1=container.pop()
            result=compute(numbers1,numbers2,postfix_list[i])
            container.push(result)
    return container.pop()
def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return  number1-number2
    elif operator == '*':
        return number1*number2
    elif operator == '/':
        return  int(number1/number2)
    elif operator == '^':
        return number1**number2
    elif operator == '%':
        return number1%number2