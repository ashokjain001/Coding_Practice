#defining a node
class Element(object):
	def __init__(self, value):
		self.value=value
		self.next=None
		#print self,self.value, self.next

#defining actual linked list
class Linkedlist(object):
	def __init__(self, head=None):
		self.head=head

	#Append a new node created above to the linked list
	def append(self, new_element):
		current=self.head

		if current:
			while current.next:
				current=current.next
			current.next=new_element
		else:
			self.head=new_element

	#get the value of the node at a given position
	def get_position(self, position):
		current = self.head
		ele_pos = 1
		while current:
			if ele_pos == position:
				return current
			current = current.next
			ele_pos+=1
		return 

	#insert at a given position	
	def insert(self, new_element, position):
		current = self.head
		ele_pos = 1
		while current:
			if ele_pos == position-1:
				new_element.next = current.next
				current.next = new_element
				return 
			else:
				ele_pos+=1
				#print ele_pos
				current = current.next

	#Print the values of the linked list###		
	def prints(self):
		current= self.head
		while current:
			print current.value,
			current=current.next
		return

	#Print the value of node in reverse order 	
	def Recursionprint(self,current):
		if current.next == None:
			print current.value,
			return
		ll.Recursionprint(current.next)
		print current.value,
		
	#delete the first node with the given value 	
	def delete(self, value):
		current = self.head
		prev = None
		while current:
			if current.value == value:
				if prev:
					prev.next  = current.next
					return 'Deleted', value
				else:
					self.head=current.next
				return 'Deleted', value
			else:
				prev = current
				current = current.next

	#Reverse the linked list
	def reverse(self):
		current = self.head
		prev = None
		while current:
			next=current.next
			current.next=prev
			prev=current
			current=next
				
		self.head = prev
		return 

	#count number of node in a linked list		
	def count(self):
		current=self.head
		count=0
		
		while current:
			count+=1
			current = current.next
		return count

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = Linkedlist(e1)
ll.append(e2)
ll.append(e3)

print 'Print linked list '
print ll.prints()
'''Print linked list 
1 2 3 None'''

# Insert node at  
print 'Insert node with value 4 at position 3',ll.insert(e4,3)

print 'Print linked list '
print ll.prints()
'''Print linked list 
1 2 4 3 None'''

# Should print 4
print 'Value of the node at position 3 is',ll.get_position(3).value
'''Value of the node at position 3 is 4'''

# number of element in linked list
print 'Number of nodes in linked list ',ll.count()
'''Number of nodes in linked list  4'''

# print the values of linkedlist in reverse order 
print 'Print the values of linkedlist in reverse order' 
print ll.Recursionprint(ll.head)
'''Print the values of linkedlist in reverse order
3 4 2 1 None'''

print 'Delete node with value 4'
print ll.delete(4)
'''Delete node with value 4
('Deleted', 4)'''

print 'Print linked list '
print ll.prints()
'''Print linked list 
1 2 3 None'''

print 'Reverse the linked list'
print ll.reverse()
print 'Printing linked list after reverse operation'
print ll.prints()
'''Printing linked list after reverse operation
3 2 1 None'''

print 'Print first node after reverse operation'
print ll.get_position(1).value
'''Print first node after reverse operation
3'''

