class Element(object):
	def __init__(self, value):
		self.value = value 
		self.next = None
		self.prev = None

class doublylinkedlist(object):
	def __init__(self, head=None):
		self.head = head 

	def append(self,new_element):
		current = self.head
		if current:
			while current.next:
				current = current.next 
			current.next = new_element
		else:
			self.head = new_element
		return ''

	def insert(self,new_element,position):
		current = self.head
		elepos = 1
		while current:
			if elepos == position-1:
				new_element.next = current.next 
				current.next.prev = new_element
				current.next = new_element
				new_element.prev = current
				return ''
			elif position == 1:
				new_element.next = self.head
				self.head = new_element
				return ''
			else:
				elepos+=1
				current=current.next

	def delete(self,value):
		current = self.head
		while current:
			if current.value == value:
				current.prev.next = current.next
				current.next.prev = current.prev
				return ''
			else:
				current = current.next

	def prints(self):
		current = self.head
		while current:
			print current.value,
			current = current.next
		return ''

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
dl = doublylinkedlist(e1)

print 'Print doubly linked list',dl.prints()
#Print doubly linked list 1 

print 'Insert node with value 4 at position 1',dl.insert(e4,1)
#Insert node with value 4 at position 1 

print 'Insert node with value 3 at position 2',dl.insert(e3,2)
#Insert node with value 3 at position 2 

print 'Append node with value 2',dl.append(e2)
#Append node with value 2

'''
dl.append(e2)
dl.append(e3)

print dl.prints()

dl.insert(e4,2)
'''
print 'Print doubly linked list',dl.prints()
#Print doubly linked list 4 3 1 2 

print 'Delete node with value 3',dl.delete(3)
#Delete node with value 3 

print 'Print doubly linked list',dl.prints()
#Print doubly linked list 4 1 2 