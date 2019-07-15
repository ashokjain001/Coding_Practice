# Array Implementation of Stack
import operator;

class Stack(object):
	def __init__(self):
		self.items = []

	def push(self,new_element):
		return self.items.append(new_element)

	def pop(self):
		return self.items.pop()	

	def top(self):
		return self.items[-1]	

	def isEmpty(self):
		return self.items==[]

	def prints(self):
		return self.items

# Applications of Stack
# String reversal using Stack
	def reverse(self,str):

		string = list(str)
		
		for i in string:
			s.push(i)

		for i in range(len(string)):
			string[i]= s.top()
			s.pop()

		return ''.join(string)

# Parantheses balancing using Stack
	def balance(self,parentheses):

		for i in parentheses:
			if i =='(':
				s.push('(')
			elif s.isEmpty() or s.top()!='(':
				return False
			else:	
				s.pop()
		if s.isEmpty():
			return True
		else:
			return False

# postfix evaluation using Stack
	def evaluatePostfix(self, exp):	
		ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div }
		for i in exp:
			if i.isdigit():
				s.push(i)
			else:
				a=s.pop()
				b=s.pop()
				remainder = ops[i](int(b),int(a))
				s.push(remainder)
		return remainder
s = Stack()

#print s.reverse('Ashok')
#print s.balance('((())))()()(())(())')
print s.evaluatePostfix('23*54*+9-')
print s.evaluatePostfix('23+')
print s.evaluatePostfix('82/')

'''
#Initializing Stack
s = Stack()

#Adding new elements to stack
s.push(1)
s.push(2)
s.push(3)
s.push(4)

#removing top element
print s.pop()
print s.pop()

#returning top element
print s.top()

#is stack empty
print s.isEmpty()

#removing top element
print s.pop()
print s.top()

print s.pop()

#is stack empty
print s.isEmpty()
'''




