from collections import deque

class Number:
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

class Plus:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Minus:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

def parse_expression(expression):
    tokens = expression.split()
    stack = []
    cur_operator = deque()
    operators = {'+': Plus, '-': Minus}

    for token in tokens:
        if token in operators:
            cur_operator.append(token)
            if len(stack) > 1:
                right = stack.pop()
                left = stack.pop()
                cur_operation = cur_operator.popleft()
                operator = operators[cur_operation](left, right)
                result = operator.interpret()
                stack.append(Number(result))
        else:
            stack.append(Number(int(token)))

    if cur_operator:
        right = stack.pop()
        left = stack.pop()
        cur_operation = cur_operator.popleft()
        result = operators[cur_operation](left, right)
        stack.append(Number(result.interpret()))

    return stack.pop()

if __name__ == "__main__":
    expression = "10 + 5 - 3"
    parsed_expression = parse_expression(expression)
    result = parsed_expression.interpret()
    print(f"Result: {result}")
