'''
Stack:
A list with the restriction that insertion and deletion can be 
performed only from one end, called top(Last In First Out).
Operations
1) Push - insert element at the top of the stack
2) Pop  - remove element from the top of the stack 
3) Top  - returns item from top of the stack
4) isEmpty - check whether stack is empty or not

Run time of all the above operation is constant time O(1).  

Application - used for function call/Recursion in the program.
			- usec it to implement undo operation in editor.
			- back button in a Browser
			- Balanced parenthesis

In linked list Implementation - 
Insertion and deletion of nodes at the end of the linked list is O(n)
Insertion and deletion of nodes at the begining of the linked list is O(1)
Implementation below is using the second approach
'''
class Element(object):
	def __init__(self,value):
		self.value = value 
		self.next = None 

class Stack(object):
	def __init__(self, head=None):
		self.head = head

	#Enter new element at the top of the Stack
	def push(self, new_element):
		current = self.head
		if current:
			new_element.next = current
			self.head = new_element
		else:
			self.head = new_element
		return ''

	#remove element from the top of the Stack	
	def pop(self):
		current = self.head
		if current:
			self.head = current.next
		return current.value

	#print the element in stack	
	def prints(self):
		current=self.head
		while current:
			print current.value,
			current = current.next
		return ''


	# print the top element of the array
	def top(self):
		current = self.head
		if current:
			return current.value
		else:
			return '' 
		return ''


# Test cases
# set up elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)

print 'top item in stack is',stack.top()
# top item in stack is 3
print 'print',stack.prints()
# print 3 2 1 
print 'Pop1',stack.pop()
# Pop1 3
print 'print',stack.prints()
# print 2 1 
print 'Pop2',stack.pop()
# Pop2 2
print 'print',stack.prints()
# print 1 
print 'pop3',stack.pop()
# pop3 1
print 'print',stack.prints()
# print 
print 'push element 4',stack.push(e4)
# push element 4 
print 'print', stack.prints()
print 'top item in stack is',stack.top()
# top item in stack is 4
# print 4 
print 'Pop4',stack.pop()
# Pop4 4
print 'print', stack.prints()
# print 


