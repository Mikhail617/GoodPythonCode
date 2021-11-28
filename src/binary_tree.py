class Node:
   def __init__(self, data):
      self._left = None
      self._right = None
      self._data = data

   @property
   def left(self):
        return self._left
    
   @left.setter
   def left(self, left):
        self._left = left

   @property
   def right(self):
        return self._right
    
   @right.setter
   def right(self, right):
        self._right = right

   @property
   def data(self):
        return self._data
    
   @data.setter
   def data(self, data):
        self._data = data

# Insert Node
   def insert(self, data):
      if self._data:
         if data < self._data:
            if self._left is None:
               self._left = Node(data)
            else:
               self._left.insert(data)
         elif data > self._data:
            if self._right is None:
               self._right = Node(data)
            else:
               self._right.insert(data)
      else:
         self._data = data

# Print the Tree
   def PrintTree(self):
      if self._left:
         self._left.PrintTree()
      print( self._data),
      if self._right:
         self._right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

# Preorder traversal
# Root -> Left ->Right
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res