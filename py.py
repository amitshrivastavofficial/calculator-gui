"""Python3 program for nth node of
inorder traversal"""

# A Binary Tree Node
# Utility function to create a
# new tree node
class newNode:

	# Constructor to create a newNode
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.visited = False

count = [0]

""" Given a binary tree, print the nth
	node of inorder traversal"""
def NthInorder(node, n):

	if (node == None):
		return

	if (count[0] <= n):

		""" first recur on left child """
		NthInorder(node.left, n)
		count[0] += 1

		# when count = n then print element
		if (count[0] == n):
			print(node.data, end = " ")

		""" now recur on right child """
		NthInorder(node.right, n)
						
# Driver Code
if __name__ == '__main__':

	root = newNode(10)
	root.left = newNode(20)
	root.right = newNode(30)
	root.left.left = newNode(40)
	root.left.right = newNode(50)

	n = 4

	NthInorder(root, n)

# This code is contributed
# by SHUBHAMSINGH10
