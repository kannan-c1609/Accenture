"""
Infix to Postfix Conversion
	Infix Expressions:
	In Infix expressions, operations are written in-between their operands.
	An expression such as A * (B + C)/D means-
	1. First add B and C together
	2. Multiply the result by A
	3. Divide by D to get the final answer
	The expression for adding the numbers 1 and 2 is “1 + 2”.
	Postfix Expressions:
	In Postfix expressions, the operators follow their operands.
	The expression for adding the numbers 3 and 4 is “3 4 + “.
	If there are multiple operations, the operator is given immediately after its second operand.
	So the expression written for “3 – 4 + 5” would be “3 4 – 5 +” in Postfix notation. Here, 4 is first subtracted from 3, then added to 5.
	Write a program that takes input as a string containing an infix expression and returns the corresponding postfix expression.
	Note:
	1. The string contains operators (+, -,/, *), parenthesis and operands. (digits).
	2. Each digit is a separate operand.
	The operator precedence is as follows:

"""


class Conversion:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        self.array = []

        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while ((not self.isEmpty()) and
                       self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))


exp = input()
obj = Conversion(len(exp))
obj.infixToPostfix(exp)