class Element(object):
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None

class BST(object):
	def __init__(self,root= None):
		self.root = root #pointer to root node and setting the tree as empty


	def insert(self, value):
		self.insert_(self.root, value)

	def insert_(self, root, value):
		
		if root == None:
			root = Element(value)
			return root   # returns the address of the root

		if root.value >= value:
			root.left = self.insert_(root.left ,value)

		if root.value < value:
			root.right = self.insert_(root.right ,value)

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
			print root.value
			self.printTree_(root.left)
			
			self.printTree_(root.right)


	def minTree(self):

		current=self.root

		if current == None:
			return 'No nodes in the Binary Search tree'

		while current.left!=None:
			current = current.left
		return current.value

	def maxTree(self):
		
		current = self.root
		if current == None:
			return 'No nodes in the Binary Search tree'

		while current.right!=None:
			current = current.right
		return current.value	


	def findheight(self):
		return self.findheight_(self.root)

	def findheight_(self, root):

		if root == None:
			return -1 

		leftHeight = self.findheight_(root.left)
		rightHeight = self.findheight_(root.right)

		return max(leftHeight,rightHeight)+1

	# depth first search
	def preorder_Traversal(self):
		return self.preorder_Traversal_(self.root)

	def preorder_Traversal_(self,root):
		
		if root!=None:
			print root.value
			self.preorder_Traversal_(root.left)
			self.preorder_Traversal_(root.right)


	def inorder_Traversal(self):
		return self.inorder_Traversal_(self.root)

	def inorder_Traversal_(self,root):

		if root!=None:
			self.inorder_Traversal_(root.left)
			print root.value
			self.inorder_Traversal_(root.right)


	def postorder_Traversal(self):
		return self.postorder_Traversal_(self.root)

	def postorder_Traversal_(self,root):

		if root!=None:
			self.postorder_Traversal_(root.left)
			self.postorder_Traversal_(root.right)
			print root.value


	# level order is a breadth first search		
	def levelOrderTraversal(self):
		queue = []
		queue.append(self.root)
		return self.levelOrderTraversal_(queue)

	def levelOrderTraversal_(self, queue):
		print queue
		if len(queue)!=0:
			current = queue[0]
		
			if current.left:
				queue.append(current.left)

			if current.right:
				queue.append(current.right)

			print current.value

			return self.levelOrderTraversal_(queue[1:])


	def levelOrderTraversalloop(self):
		queue = []
		queue.append(self.root)

		while len(queue)!=0:
			current = queue[0]
			print current.value

			if current.left!=None:
				queue.append(current.left)

			if current.right!=None:	
				queue.append(current.right)

			queue=queue[1:]




e1 = Element(15)
root = BST(e1)

root.insert(10)
root.insert(20)
root.insert(8)
root.insert(9)
root.insert(19)
root.insert(21)
root.insert(25)
root.insert(5)


root.printTree()

print 'Minimum value node in the Tree is', root.minTree()

print 'Maximum value node in the Tree is' ,root.maxTree()

print 'Height of the Tree is', root.findheight()

print 'preorder Traversal of the Tree', root.preorder_Traversal()

print 'Inorder Traversal of the Tree', root.inorder_Traversal()

print 'postorder Traversal of the Tree', root.postorder_Traversal()

print root.levelOrderTraversal()

print root.levelOrderTraversalloop()

#print root.search(21)



