from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):

	class Node:
		def __init__(self, element, parent = None, left = None, right = None):

			self._element = element
			self._parent = parent
			self._left = left
			self._right = right


	class Position(BinaryTree.Position):

		def __init__(self, node, container):
			self._container = container
			self._node = node

		################# DOUBT ###############
		def element(self):			   #
			return self._node._element				   #
		#######################################


		def __eq__(self, other):

			return type(other) is type(self) and other._node is self._node


	def _validate(self, p):
		if not isinstance(p, self.Position):
			raise TypeError('P must be proper Position type.')

		if p._container is not self:
			raise ValueError('p does not belong to valid container.')

		if p._node._parent is p._node:
			raise ValueError('p is no longer valid.')

		return p._node 


	def _make_position(self, node):
		return self.Position(self, node) if node is not None else None



	def __init__(self):

		self._root = None
		self._size = 0


	def __len__(self):
		return self._size


	def root(self):
		return self._make_position(self._root)


	def parent(self, p):
		node = self._validate(p)
		# if node == self._root:
		# 	return None

		# else:
		return self._make_position(self._node._parent)


	def left(self, p):
		node = self._validate(p)

		# if node._left is not None:
		return self._make_position(node._left)


	def right(self, p):
		node = self._validate(p)
		return self._make_position(node._right)


	def num_children(self, p):
		node = self._validate(p)

		num = 0

		if node._left is not None:
			num += 1

		if node._right is not None:
			num += 1

		return num


	def _add_root(self, e):

		if self._root is not None:
			raise TypeError("Root not exist.")

		node = self.Node(e)
		self._size += 1

		self._root = node 

		return self._make_position(self._root)


	def _add_left(self, p, e):

		node = self._validate(p)

		if node._left is not None:
			raise TypeError("Left already exist.")

		node._left = self.Node(e, node)
		self._size += 1

		return self._make_position(node._left)


	def _add_right(self, p, e):
		node = self._validate(p)

		if node._right is not None:
			raise TypeError("Right already exist.")

		node._right = self.Node(e, node)
		self._size += 1

		return self._make_position(node._right)

	def _replace(self, p, e):
		node = self._validate(p)

		value = node._element

		node._element = e 

		return value 

	def _delete(self, p):
		node = self._validate(p)

		if self.num_children(node) == 2:
			raise ValueError("This node have two childrens.")

		if node._left is not None:
			child = node._left

		else:

			child = node._right


		if child is not None:
			child._parent = node._parent

		if node is self._root:
			self._root = child 

		else:
			parent = node._parent

			if node is parent._left:
				parent._left = child

			else:
				parent._right = child 


		self._size -= 1
		# node._parent = node          # Doubt.

		return node._element


	def _attach(self, p, t1, t2):

		node = self._validate(p)

		if not self.is_leaf(node):
			raise TypeError("Node must be leaf.")

		if not( type(self) is type(t1) and type(self) is type(t2)):
			raise ValueError("All tree must be of same type.")

		self._size += len(t1) + len(t2)

		if not t1.is_empty():
			t1._root._parent = node 
			node._left = t1._root

			t1._root = None

			t1._size = 0

		if not t2.is_empty():
			t2.root._parent = node 

			node._right = t2._root
			t2._root = None 
			t2._size = 0


	def inorder(self):
		if not self.is_empty():
			for p in self._subtree(self.root()):
				print(p.element())
				


	def _subtree(self, p):
		print(p.element())
		for c in self.children(p):
			for other in self._subtree(c):
				print(other.element())



if __name__ == "__main__":
	obj = LinkedBinaryTree()

	# print(obj.root())

	print(obj._add_root(5))
	print(obj._add_left(obj.left(obj.root()), 7))
	print(len(obj))

	print(obj.inorder())







