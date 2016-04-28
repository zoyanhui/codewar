class Calculator(object):
    def pop_calc(self, operators, operands, cur_operator, reverse = False):
        while operators:
            if (cur_operator == '/' or cur_operator == '*') and (operators[-1] == '+' or operators[-1] == '-'):
                break
            operator = operators.pop()
            if operator == '*':
                operands.append(operands.pop() * operands.pop())
            elif operator == '/':
                temp = operands.pop()
                operands.append(temp / operands.pop() if reverse else operands.pop() / temp)
            elif operator == '+':
                operands.append(operands.pop() + operands.pop())
            else:
                r = -operands.pop() + operands.pop()
                operands.append(-r if reverse else r)

    def evaluate(self, string):
        expr = string.split(" ")
        operators = []
        operands = []
        for e in expr:
            if not e:
                continue
            if e == '*' or e == '/':
                self.pop_calc(operators, operands, e)
                operators.append(e)
            elif e == '+' or e == '-':
                self.pop_calc(operators, operands, e)
                operators.append(e)
            else:
                operands.append(float(e))
        operands.reverse()
        operators.reverse()
        self.pop_calc(operators, operands, None, True)
        return round(operands.pop(),4)
