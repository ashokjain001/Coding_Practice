class newelement(object):
	"""docstring for ClassName"""
	def __init__(self, value):
		self.value = value 
		self.next = None
		self.prev = None

class doublylinkedlist(object):
	"""docstring for ClassName"""
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
		return 

	def insert(self,new_element,position):
		current = self.head
		elepos = 1
		while current:
			if elepos == position-1:
				new_element.next = current.next 
				current.next.prev = new_element
				current.next = new_element
				new_element.prev = current
				return 
			elif position == 1:
				new_element.next = self.head
				self.head = new_element
				return
			else:
				elepos+=1
				current=current.next
		else:
			self.head = new_element
			return

	def prints(self):
		current = self.head
		while current:
			print current.value
			current = current.next
		return 

# Test cases
# Set up some Elements
e1 = newelement(1)
e2 = newelement(2)
e3 = newelement(3)
e4 = newelement(4)


dl = doublylinkedlist(e1)

dl.insert(e4,1)
'''
dl.append(e2)
dl.append(e3)

print dl.prints()s

dl.insert(e4,2)
'''
print dl.prints()