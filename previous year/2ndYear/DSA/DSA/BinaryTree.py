from Tree import Tree

class BinaryTree(Tree):


	def left(self, p):
		raise NotImplementedError('Yet not implemented')

	def right(self, p):
		raise NotImplementedError('Yet not implemented')

	def siblings(self, p):
		parent = self.parent(p)
		if parent is None:
			return None 

		else:
			if p == self.right(parent) :
				return self.left(parent)

			else:
				return self.right(parent)


	def children(self, p):
		if self.left(p) is not None:
			yield self.left(p)

		if self.right(p) is not None:
			yield self.right(p)


	