class Element(object):
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None

class BST(object):
	def __init__(self,root= None):
		self.root = root #pointer to root node and setting the tree as empty


	#insert using while loop
	def insertLoop(self, value):
		current = self.root
		parent = None
		
		while 1:	
			parent = current 
			if current.value > value:
				current = current.left 	
				if current == None:
					parent.left = Element(value)
					return current
					
			if current.value < value:
				current = current.right
				print current, 'Current'
				if current == None:
					parent.right = Element(value)
					return current

	#Insert using Recursion	
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
			return root
		
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
		current = self.root
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
		
		if len(queue)!=0:
			current = queue[0]
		
			if current.left:
				queue.append(current.left)

			if current.right:
				queue.append(current.right)

			print current.value

			return self.levelOrderTraversal_(queue[1:])

	#level order traversal using loop 
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

	# Check if a given binary tree is BST
	'''Trick is to make sure that root of left sub tree is less than root node, and root of right subtree 
	is greater than root node'''

	def isBST(self):
		return self.isBST_(self.root, -100000, 1000000)

	def isBST_(self, root, min, max):
		if root == None:
			return True

		if (root.value > min and root.value < max):
			print root.value, min, max
			return self.isBST_(root.left, min, root.value) and self.isBST_(root.right, root.value, max)
		return False


	#Delete node
	'''
	There are 3 cases to delete a node in Binary search tree
	1) Delete leaf node, remove reference of the node from its parents. 
	2) Delete node with one child, link its parent to its only child.
	3) Delete node with two child, find min in the right subtree and replace it with the node or find the max in the left subtree and 
	   replace it with the node. 
	'''
	def delete(self, value):
		return self.delete_(self.root, value)

	def delete_(self, root, value):

		#print root.value, value, root
		if root == None:
			print 'asdfsd'
			return 

		if root.value >value:
			print root.value 
			root.left = self.delete_(root.left, value)

		elif root.value < value:
			print root.value 
			root.right = self.delete_(root.right, value)

		else:

			if not root.right:
				return root.left

			if not root.left:
				return root.right	

			temp_root = root.right
			min_val = temp_root.value

			while temp_root.left:
				temp_root = temp_root.left
				min_val = temp_root.value
				
			root.value = min_val 
			root.right = self.delete_(root.right,root.value)
			
		return root

	def inorderSuccessor(self, value):
		return self.inorderSuccessor_(self.root,value)

	def inorderSuccessor_(self,root,value):
		current = self.search(value)
		
		if current == None:
			return False

		if current.right!=None:
			current = current.right
			while current.left:
				current = current.left
			return current.value, 'is the successor of', value

		if current.right==None:
			ancestor = self.root
			successor = None

			while ancestor!=current:
				if current.value<ancestor.value:
					successor = ancestor
					ancestor=ancestor.left
					print successor.value, 'successor', ancestor.value, 'ancestor'
				else:
					ancestor=ancestor.right

		return successor.value, 'is the successor of ', current.value


e1 = Element(15)
root = BST(e1)

root.insert(10)
root.insert(20)
root.insert(8)
root.insert(19)
root.insert(21)
root.insert(25)
root.insert(5)
root.insert(12)
root.insert(11)

'''
root.insertLoop(10)
root.insertLoop(20)
root.insertLoop(8)
root.insertLoop(9)
root.insertLoop(19)
root.insertLoop(21)
root.insertLoop(25)
root.insertLoop(5)
root.insertLoop(22)
root.insertLoop(26)

root.printTree()
'''
root.printTree()

#print root.delete(20)
#print root.minTree()

print root.inorderSuccessor(8)
print root.inorderSuccessor(10)
print root.inorderSuccessor(12)
print root.inorderSuccessor(11)
'''

print 'Minimum value node in the Tree is', root.minTree()

print 'Maximum value node in the Tree is' ,root.maxTree()

print 'Height of the Tree is', root.findheight()

print 'preorder Traversal of the Tree', root.preorder_Traversal()

print 'Inorder Traversal of the Tree', root.inorder_Traversal()

print 'postorder Traversal of the Tree', root.postorder_Traversal()

print root.levelOrderTraversal()

print root.levelOrderTraversalloop()
'''
#print root.search(21)

#print root.isBST()


