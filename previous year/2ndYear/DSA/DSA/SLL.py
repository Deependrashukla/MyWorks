from nodes import SingalNode

class Sll(object):
	def __init__(self):

		
		# node = SingalNode()
		self._size = 0
		self._head = None


	def _insertElementAtHead(self, element):
		node = SingalNode()
		node.element = element
		self._size += 1
		node.next1 = self._head
		self._head = node 


	def _insertElementAtTail(self, element):
		node = SingalNode()
		node.element = element
		# print(1)

		self._size += 1

		current = self._head
		# print(1) 
		# print(current.next1)
		print(current)

		if current.next1 is None:
			current.next1 = node

		else:

			while current.next1:
				# print('hii')
				
				# print(current.next1)
				if current.next1.next1 == None: 
					# print(node)
					current.next1.next1 = node
					break
				current = current.next1
				print(current)
				# print(current)


	def _insertElementBtwNodes(self, previous, after):
		pass


	def _deleteAtTail(self):

		current = self._head

		while current.next1.next1:
			value = current.next1

			current.next1 = None
			return value._element


	def _deleteAtHead(self):

		current = self._head
		# print('current')

		value = current._element

		self._head = current.next1

		return value







	def __len__(self):
		obj = self._head 
		lenght = 0
		while obj.next1 != None:
			lenght += 1
			obj = obj.next1

		return (self._size)


if __name__ == '__main__':
	obj = Sll()
	obj._insertElementAtHead(5)
	# obj._insertElementAtHead(5)
	obj._insertElementAtTail(6)
	obj._insertElementAtTail(7)
	obj._insertElementAtTail(8)
	obj._insertElementAtTail(9)
	obj._insertElementAtTail(10)
	print(obj._deleteAtHead())
	print(obj._deleteAtHead())
	print(obj._deleteAtHead())
	print(obj._deleteAtHead())
	print(obj._deleteAtHead())
	print(obj._deleteAtHead())

	# print(len(obj))
