import unittest
from Trees.printTree import TreeNode, Solution


class TestPrintTree(unittest.TestCase):
	def testCase1:
		#single node as tree
		root = TreeNode(1)
		self.answer = [['1']]
		self.input = Trees.printTree(root)
		assert self.input == self.answer

	def testCase2:
		#2. full balanced tree
		root = TreeNode(1)
		root.left = TreeNode(2)
		root.right = TreeNode(3)
		root.left.left = TreeNode(4)
		root.left.right=TreeNode(5)
		root.right.left=TreeNode(6)
		root.right.right=TreeNode(7)
		self.answer = [['|', '|', '|', '1', '|', '|', '|'],
                               ['|', '2', '|', '|', '|', '3', '|'],
                               ['4', '|', '5', '|', '6', '|', '7']]
       		self.input = Trees.printTree(root)
		assert self.input == self.answer
	 def testCase3:
     		#3. left branches tree
		root=TreeNode(1)
		root.left=TreeNode(2)
		root.left.left=TreeNode(3)
		root.left.left.left=TreeNode(4)
		self.answer = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                               ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                               ['|', '3', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                               ['4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
                self.input = Trees.printTree(root)
		assert self.input == self.answer
	def testCase4:
		#4. irregular tree
		root =TreeNode(1)
		root.left=TreeNode(2)
		root.right=TreeNode(3)
		root.left.right=TreeNode(4)
		root.right.left=TreeNode(5)
		root.right.left.right=TreeNode(6)
		self.answer = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                      	       ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                               ['|', '|', '|', '|', '|', '4', '|', '|', '|', '5', '|', '|', '|', '|', '|'],
                               ['|', '|', '7', '|', '8', '|', '|', '|', '|', '|', '6', '|', '|', '|', '|']]
        	self.input = Trees.printTree(root)
		assert self.input == self.answer
