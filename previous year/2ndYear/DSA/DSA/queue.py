from Errors import QueueIsFull, QueueIsEmpty

class Queue(object):
	Default_size = 8
	def __init__(self):
		self._size = 0
		self._data = [None] * Queue.Default_size
		self._front = 0
		# self._rare = self._size - 1

	def dequeue(self):
		# index = (self._size + self._front) % Queue.Default_size

		

		# self._data[index] = None

		if self.is_empty():
			# self._front = 0
			raise QueueIsEmpty('Queue is Empty ')

		value = self._data[self._front]
		self._front = (self._front + 1) % len(self._data)
		self._size -=1

		return value

	def enqueue(self, element):
		# print(self._size, self._front)

		index = (self._size + self._front) % len(self._data)


		self._data[index] = element
		# self._front += 1
		self._size += 1

		if len(self) == len(self._data) - 1:
			self._resize(2 * self._size)


	def __len__(self):

		return self._size


	def is_empty(self):
		return self._size == 0

	def _resize(self, cap):
		value = self._data
		self._data = [None] * cap

		for i in range(len(value)):
			self._data[i] = value[self._front]

			self._front = (self._front + 1) % self.Default_size


		self._front = 0



if __name__ == '__main__':
	obj = Queue()

	obj.enqueue(5)
	print(len(obj))

	print(obj.dequeue())

if __name__ == '__main__':
    # creating the objects of queue.
    queue = Queue()
    # queue.dequeue()     # testing error for dequeue on empty queue
    queue.enqueue(24)
    queue.enqueue(465)      # testing addition of element to queue.
    queue.enqueue(234)
    queue.enqueue(4659)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    print(len(queue))       # testing length of the queue.
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(len(queue))
    # print(queue._capacity)
    # print(queue.is_empty())        # testing is_empty function.
    # ensuring that the implemetation is circular.
    queue.enqueue(546)
    queue.enqueue(54986)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    print(len(queue))
    # print(queue._capacity)
    # print(queue.first())     




################## MY MISTAKES #####################

# 1.) I was incrasing the front when i was doing enque. but in enque element come to queue by rear not from the front.
# 2.) I was confusing my self with the size of underline array and the size of the queue.
