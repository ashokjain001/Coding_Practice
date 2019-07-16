'''
Queue is a Abstract Data type.

A list with the restriction that insertion can be performed at one end(Rear)
and deletion can be performed only from one end(Front) First In First Out.
Operations
1) Enqueue - insert element at the rear of the list
2) Dequeue  - remove element from the front of the list 
3) Front  - returns item from front of the queue
4) isEmpty - check whether queue is empty or not

This is a linked list implementation of Queue and in order to achieve O(1) run time 
we are using a rear variable to actively store the reference to the last element in queue.

'''
class Element(object):
	def __init__(self,value):
		self.value = value 
		self.next = None 

class Queue(object):
	def __init__(self, head=None):
		self.head = head
		self.rear = head

	def enqueue(self, new_element):

		current = self.head
		last = self.rear

		if last:
			last.next = new_element
			last = last.next
			self.rear = last

		self.head = new_element
		self.rear = new_element	

		return 'last value',last.value

	def dequeue(self):
		current = self.head

		if current:
			self.head = current.next
		return 

	#print the element in Queue	
	def prints(self):
		current=self.head
		while current:
			print current.value,
			current = current.next
		return ''
	
# Test cases
# set up elements
e1 = Element(1)

e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a queue
queue = Queue(e1)

# Test queue functionality
print queue.enqueue(e2)
print queue.enqueue(e3)

# enqueue item in queue is 3
print 'print',queue.prints()
# print 3 2 1 
print 'dequeue1',queue.dequeue()
# dequeue1 3
print 'print',queue.prints()
# print 2 1 
print 'dequeue2',queue.dequeue()
# dequeue2 2
print 'print',queue.prints()
# print 1 
print 'dequeue3',queue.dequeue()
# dequeue3 1
print 'print',queue.prints()
# print 
print 'push element 4',queue.enqueue(e4)
# push elemenst 4 
print 'print', queue.prints()
#print 'enqueue item in queue is',queue.enqueue()
# enqueue item in queue is 4
# print 4 
print 'dequeue4',queue.dequeue()
# dequeue4 4
print 'print', queue.prints() 

