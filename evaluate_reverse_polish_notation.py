class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']

        for t in tokens:
            if t in op:
                x, y = int(stack.pop()), int(stack.pop())
                if t == '+':
                    stack.append(x + y)
                if t == '-':
                    stack.append(y - x)
                if t == '*':
                    stack.append(x * y)
                if t == '/':
                    stack.append(y / x)
            else:
                stack.append(t)
        return int(stack[0])
            