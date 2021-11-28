import sys
sys.path.append("../src/")
import binary_tree
import unittest

class BinaryTreeTesting(unittest.TestCase):
	def test_binary_tree_inorder_traversal(self):
		root = binary_tree.Node(11)
		root.insert(22)
		root.insert(44)
		root.insert(33)
		root.insert(55)
		root.insert(77)
		root.insert(66)
		root.insert(99)
		root.insert(88)
		root.insert(0)
		self.assertEqual([0, 11, 22, 33, 44, 55, 66, 77, 88, 99], root.inorderTraversal(root))

	def test_binary_tree_preorder_traversal(self):
		root = binary_tree.Node(11)
		root.insert(22)
		root.insert(44)
		root.insert(33)
		root.insert(55)
		root.insert(77)
		root.insert(66)
		root.insert(99)
		root.insert(88)
		root.insert(0)
		self.assertEqual([11, 0, 22, 44, 33, 55, 77, 66, 99, 88], root.preorderTraversal(root))

	def test_binary_tree_postorder_traversal(self):
		root = binary_tree.Node(11)
		root.insert(22)
		root.insert(44)
		root.insert(33)
		root.insert(55)
		root.insert(77)
		root.insert(66)
		root.insert(99)
		root.insert(88)
		root.insert(0)
		self.assertEqual([0, 33, 66, 88, 99, 77, 55, 44, 22, 11], root.postorderTraversal(root))

if __name__ == '__main__':
	unittest.main()