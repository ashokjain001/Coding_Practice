class Element(object):
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None

class BST(object):
	def __init__(self,root= None):
		self.root = root #pointer to root node and setting the tree as empty

	def insert(self, new_element=None):
		self.insert_(self.root, new_element)

	def insert_(self, root=None, new_element=None):
		
		if root == None:
			root = new_element
			return root   # returns the address of the root

		if root.value >= new_element.value:
			root.left = self.insert_(root.left ,new_element)

		if root.value < new_element.value:
			root.right = self.insert_(root.right ,new_element)

		return root

	def search(self, value):
		return self.search_(root=self.root, value=value)

	def search_(self,root=None,value=None):
			
		if root == None:
			return False

		if root.value == value:
			return True	
		
		if root.value >= value:
			return self.search_(root.left,value)

		if root.value < value:
			return self.search_(root.right,value)

	def printTree(self):
		if root != None:
			self.printTree_(self.root)

	def printTree_(self,root=None):
		if root != None:
			self.printTree_(root.left)
			print root.value
			self.printTree_(root.right)




e1 = Element(15)
e2 = Element(10)
e3 = Element(20)
e4 = Element(8)
e5 = Element(9)
e6 = Element(19)
e7 = Element(21)
e8 = Element(25)

root = BST(e1)

root.insert(new_element=e2)
root.insert(new_element=e3)
root.insert(new_element=e4)
root.insert(new_element=e5)
root.insert(new_element=e6)
root.insert(new_element=e7)
root.insert(new_element=e8)
#print root.search(21)

root.printTree()


