class Calculator(object):
    def evaluate(self, string):
        expr = string.split(" ")
        operators = []
        operands = []
        preoperator = None
        for e in expr:
            if not e:
                continue
            if e == '*' or e == '/':
                preoperator = e
            elif e == '+' or e == '-':
                operators.append(e)
            else:
                if preoperator == '*':
                    r = operands.pop() * float(e)
                elif preoperator == '/':
                    r = operands.pop() / float(e)
                else:
                    r = float(e)
                operands.append(r)
                preoperator = None
        operands.reverse()
        for operator in operators:
            if operator == '+':
                operands.append(operands.pop() + operands.pop())
            else:                
                operands.append(operands.pop() - operands.pop())
        return  round(operands.pop(), 4) if operands else 0
