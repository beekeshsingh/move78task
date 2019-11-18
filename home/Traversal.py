#new node 
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

# Function to insert nodes in level(position) order 
def insertLevelOrder(arr, root, i, n): 
	# Base case for recursion 
	if i < n: 
		temp = newNode(arr[i]) 
		root = temp 
		# insert left child 
		root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
		# insert right child 
		root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
	return root 

# Tree Traversal class 
class Traversal:
	# Inorder Traversal function
	# Left -> Root -> Right
	def inorderTraversal(self, root):
		response = []
		if root:
			response = response + self.inorderTraversal(root.left)
			response.append(root.data)
			response = response + self.inorderTraversal(root.right)
		return response

	# Postorder traversal function
	# Left -> Right -> Root
	def postorderTraversal(self, root):
		response = []
		if root:
			response = response + self.postorderTraversal(root.left)
			response = response + self.postorderTraversal(root.right)
			response.append(root.data)
		return response

	# Preorder Traversal function
	# Root -> Left -> Right
	def preorderTraversal(self, root):
		response = []
		if root != None:
			response.append(root.data)
			response = response + self.preorderTraversal(root.left)
			response = response + self.preorderTraversal(root.right)
		return response

# Below code is testing purpose only
if __name__ == '__main__': 
	arr = [1, 2, 3]
	n = len(arr) 
	root = None
	travel = Traversal()
	root = insertLevelOrder(arr, root, 0, n)
	print('In-Order Traversal -> ', travel.inorderTraversal(root))
	root = insertLevelOrder(arr, root, 0, n)
	print('Post-Order Traversal -> ', travel.postorderTraversal(root))
	root = insertLevelOrder(arr, root, 0, n)
	print('Pre-Order Traversal -> ', travel.preorderTraversal(root))
# This code is contributed by PranchalK 
