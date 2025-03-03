class DoublyLinkedList:

	class Node:
		def __init__(self):
			self._previous = None
			self._next = None
			self._element = None

		@property
		def element(self):
			return self._element

	def __init__(self):

		self._header = self.Node()
		self._tailer = self.Node()
		self._header._next = self._tailer
		self._tailer._previous = self._header
		self._size = 0


	def _insertBtwNodes(self, predecessor, sucessor, element):
		node = self.Node()
		node._element = element 
		node._previous = predecessor
		node._next = sucessor
		predecessor._next = node 
		sucessor._previous = node 
		self._size += 1


	def _deleteBtwNodes(self, predecessor, sucessor):
		value = predecessor._next._element
		predecessor._next = sucessor
		sucessor._previous = predecessor

		return value


	def __len__(self):
		return self._size



if __name__ == '__main__':
	obj = DoublyLinkedList()

	obj._insertBtwNodes(obj._tailer, obj._header, 5)
	print(len(obj))

	print(obj._deleteBtwNodes(obj._tailer, obj._header))
	



		