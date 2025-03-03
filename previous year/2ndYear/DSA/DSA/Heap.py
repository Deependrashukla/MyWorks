# class HeapArray:
# 	def __init__(self):
# 		self._lst = []
# 		self._size = 0
# 		self._root = 0

# 	def insert(self, element):
# 		self._size += 1
# 		self._lst.append(element)

# 	def delete(self):
# 		return self._lst.pop()

# 	# def downHeap(self, parentIndex):
# 	# 	try:
# 	# 		child1index = 2 * parentIndex + 1
# 	# 		child2index = 2 * parentIndex + 2

# 	# 		child1value = self._lst[child1index]
# 	# 		child2value = self._lst[child2index]
# 	# 		self._lst[parentIndex]

# 	# 	except:
# 	# 		return

# 	# 	if min(child1value, child2value) < self._lst[parentIndex]:
# 	# 		if child1value < child2value:
# 	# 			self._lst[child1index], self._lst[parentIndex] = self._lst[parentIndex], self._lst[child1index]

# 	# 			self.downHeap(child1index)

# 	# 		elif child1value > child2value:
# 	# 			self._lst[child2index], self._lst[parentIndex] = self._lst[parentIndex], self._lst[child2index]

# 	# 			self.downHeap(child2index)


# 	# def downHeap(self, parentIndex):
# 	# 	leftChildIndex = 2 * parentIndex + 1
# 	# 	rightChildIndex = 2 * parentIndex + 2

# 	# 	smallestChild = parentIndex
		

# 	# 	if leftChildIndex < self._size and self._lst[leftChildIndex] < self._lst[smallestChild]:
# 	# 		smallestChild = leftChildIndex

# 	# 	if rightChildIndex < self._size and self._lst[rightChildIndex] < self._lst[smallestChild]:
# 	# 		smallestChild = rightChildIndex

# 	# 	print(smallestChild, parentIndex, self._lst)
# 	# 	if smallestChild != parentIndex:
# 	# 		self._lst[parentIndex], self._lst[smallestChild] = self._lst[smallestChild], self._lst[parentIndex]
# 	# 		self.downHeap(smallestChild)

# 	def downHeap(self, parentIndex):
# 	    leftChildIndex = 2 * parentIndex + 1
# 	    rightChildIndex = 2 * parentIndex + 2

# 	    smallestChild = parentIndex

# 	    if leftChildIndex < self._size and self._lst[leftChildIndex] < self._lst[smallestChild]:
# 	        smallestChild = leftChildIndex

# 	    if rightChildIndex < self._size and self._lst[rightChildIndex] < self._lst[smallestChild]:
# 	        smallestChild = rightChildIndex

# 	    if smallestChild != parentIndex:
# 	        self._lst[parentIndex], self._lst[smallestChild] = self._lst[smallestChild], self._lst[parentIndex]
# 	        self.downHeap(smallestChild)



# if __name__ == '__main__':
# 	obj = HeapArray()
# 	obj.insert(5)
# 	obj.insert(4)
# 	obj.insert(7)
# 	obj.insert(9)
# 	obj.insert(2)
# 	obj.insert(3)
# 	obj.insert(11)

# 	print(obj._lst)
# 	obj.downHeap(0)
# 	print(obj._lst)


class HeapArray:
	def __init__(self):
		self._lst = []
		self._size = 0
		self._root = 0

	def insert(self, element):
		self._size += 1
		self._lst.append(element)
		self.upHeap(self._size-1)

	def delete(self):
		self._lst[0], self._lst[self._size-1] = self._lst[self._size-1], self._lst[0]
		self._lst.pop()
		self._size -= 1
		self.downHeap(0)

	def upHeap(self, currentIndex):
		parentIndex = (currentIndex-1)//2
		while(currentIndex>0 and self._lst[currentIndex]<self._lst[parentIndex]):
			self._lst[currentIndex], self._lst[parentIndex] = self._lst[parentIndex], self._lst[currentIndex]
			currentIndex = parentIndex
			parentIndex = (currentIndex-1)//2

	def downHeap(self, parentIndex):
		leftChildIndex = 2 * parentIndex + 1
		rightChildIndex = 2 * parentIndex + 2

		smallestChild = parentIndex

		if leftChildIndex < self._size and self._lst[leftChildIndex] < self._lst[smallestChild]:
			smallestChild = leftChildIndex

		if rightChildIndex < self._size and self._lst[rightChildIndex] < self._lst[smallestChild]:
			smallestChild = rightChildIndex

		if smallestChild != parentIndex:
			self._lst[parentIndex], self._lst[smallestChild] = self._lst[smallestChild], self._lst[parentIndex]
			self.downHeap(smallestChild)

	def __len__(self):
		return self._size

if __name__ == '__main__':
	obj = HeapArray()
	obj.insert(5)
	obj.insert(4)
	obj.insert(7)
	obj.insert(9)
	obj.insert(2)
	obj.insert(3)
	obj.insert(11)

	print(obj._lst)
	# obj.downHeap(0)
	# obj.delete()
	print(obj._lst)

