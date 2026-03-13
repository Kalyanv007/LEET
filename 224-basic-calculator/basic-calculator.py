class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for c in s:

            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '+':
                result += sign * num
                num = 0
                sign = 1

            elif c == '-':
                result += sign * num
                num = 0
                sign = -1

            elif c == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif c == ')':
                result += sign * num
                num = 0

                result *= stack.pop()
                result += stack.pop()

        result += sign * num
        return result