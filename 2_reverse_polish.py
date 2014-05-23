#!/usr/bin/python
import pdb
class Solution:
    def __init__(self):
	self.operand_stack = []

    def getResult(self, no_1, no_2, op):
        "Calculate the result. This is cleaner, Dont use eval"

	if op == '+': return no_1 + no_2
	elif op == '-': return no_2 - no_1
        elif op == '*': return no_1 * no_2
        elif op == '/':
	    if no_1 is not 0:
	        return int(float(no_2) / no_1) # Round up -6/132 to 0 instead of -1

    def evalRPN(self, tokens):
        """To evaluate an expression in RPN
	   1. If you encounter an operand, push it on the operand stack
	   2. If you encounter an operator, pop 2 operands and evaluate the result
	   3. Push the result back on the stack and continue"""

	res = 0
	for tok in tokens:
	    if tok in "+-*/":
                no_1 = self.operand_stack.pop()
		no_2 = self.operand_stack.pop()
		res = self.getResult(no_1, no_2, tok)
		self.operand_stack.append(res)
	    else:
		self.operand_stack.append(int(tok)) # Push the operand on the stack as an int
        return self.operand_stack.pop()


so = Solution()
tokens1 = ["2", "1", "+", "3", "*"] # -> ((2 + 1) * 3) -> 9 
tokens2 = ["4", "13", "5", "/", "+"] #-> (4 + (13 / 5)) -> 6 (See 13/5)
tokens3 = ["18"]
tokens4 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ans1 = so.evalRPN(tokens1)
ans2 = so.evalRPN(tokens2)
ans3 = so.evalRPN(tokens3)
ans4 = so.evalRPN(tokens4)
assert ans1 == 9
assert ans2 == 6
assert ans3 == 18
assert ans4 == 22
print "RPN%s = %s" %(tokens1, ans1)
print "RPN%s = %s" %(tokens2, ans2)
print "RPN%s = %s" %(tokens3, ans3)
print "RPN%s = %s" %(tokens4, ans4)
