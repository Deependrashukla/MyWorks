from Errors import StackIsEmpty
from Errors import StackIsFull


class StaticStack(object):

	def __init__(self, size = 8):
		self._size = size
		self._data = [None] * self._size
		self._index = 0

	def push(self, element):
		if self._index == self._size:
			raise StackIsFull('Stack is Full')

		self._data[self._index] = element
		self._index += 1

	def pop(self):
		if self.is_empty():
			raise StackIsEmpty('Stack is Empty')

		self._index -= 1
		value = self._data[self._index]
		self._data[self._index] = None

		return value

	def __len__(self):
		return self._index + 1

	def is_empty(self):
		return len(self) == 0 

	def top(self):
		if self.is_empty():
			raise StackIsEmpty('Stack is Empty')

		return self._data[self._index - 1]

class Stack(object):
	def __init__(self):
		self._data = []

	def pop(self):
		if self.is_empty():
			raise StackIsEmpty('Stack is empty')
		return self._data.pop()

	def push(self, element):
		self._data.append(element)

	def __len__(self):
		return len(self._data)

	def top(self):
		if self.is_empty():
			raise StackIsEmpty('Stack is empty')
		return self._data[-1]

	def is_empty(self):
		return len(self) == 0

if __name__ == '__main__':
	# obj = Stack()
	obj1 = StaticStack(10)
	# print(len(obj1))


	for i in range(10):
		obj1.push(i)
		# print(obj1.top(), obj1._index)

	# obj1.push(1)

	# print(obj1.pop())

	for _ in range(10):
	# 	pass

		print(obj1.pop(), len(obj1), obj1.top(), obj1.is_empty(), obj1._index)
	# print(len(obj))

	# print(obj.pop())
	# print(obj.pop())



