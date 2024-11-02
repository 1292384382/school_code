# 假设 Stack 类已经定义
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# 创建一个栈实例
postfix_stack = Stack()

# 假设最开始将 3 和 4 压入栈中
postfix_stack.push(3)
postfix_stack.push(4)

# 输入后缀表达式
tokens = ['*', 6, '/', 3, '+']

# 处理后缀表达式
for token in tokens:
    if isinstance(token, (int, float)):  # 如果是操作数
        postfix_stack.push(token)  # 压入栈
    else:  # 如果是运算符
        # 弹出两个操作数
        operand2 = postfix_stack.pop()
        operand1 = postfix_stack.pop()

        # 根据运算符进行计算
        if token == '*':
            result = operand1 * operand2
        elif token == '/':
            result = operand1 / operand2
        elif token == '+':
            result = operand1 + operand2
        elif token == '-':
            result = operand1 - operand2

        # 将结果压入栈中
        postfix_stack.push(result)

# 计算完成后，栈中应只有一个值
final_result = postfix_stack.pop()

# 输出最终结果
print(final_result)  # 输出: 5