class Tree:
	class Position:
		# def __init__(self, element, container):
		# 	self._element = element
		# 	self._container = container


		def element(self, position):
			raise NotImplementedError('Yet not implemented')
			# return position._element

		def __eq__(self, other):
			raise NotImplementedError('Yet not implemented')

		def __nq__(self, other):
			return not(self == other)


	def root(self):
		raise NotImplementedError('Yet not implemented')

	def parent(self, pos):
		raise NotImplementedError('Yet not implemented')

	def num_children(self, pos):
		raise NotImplementedError('Yet not implemented')

	def children(self, pos):
		raise NotImplementedError('Yet not implemented')

	def positions(self):
		raise NotImplementedError('Yet not implemented')

	def __len__(self):
		raise NotImplementedError('Yet not implemented')

	def is_root(self, p):
		return self.root() == p

	def is_empty(self):
		return len(self) == 0

	def is_leaf(self, p):
		return self.num_children(p) == 0

	def depth(self, p):
		if self.is_root(p):
			return 0

		else:
			return 1 + self.depth(self.parent(p))


	def height1(self, p):

		if self.is_leaf(p):
			return 0

		else:
			return 1 + max(self.height(self.children(c) for c in self.children(p)))


	def height2(self):
		"""
		Return the height of tree.
		"""
		return max(self.depth(c) for c in self.positions() if c is self.is_leaf(c))