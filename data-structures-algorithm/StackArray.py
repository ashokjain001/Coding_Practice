# Array Implementation of Stack

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

