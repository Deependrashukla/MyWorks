from queue import Queue
# from Heap import HeapArray
from HeapPriority import HeapPriorityQueue

class timeError(BaseException):
	pass

class BurgerError(BaseException):
	pass

class Customer(object):
	def __init__(self, id, t, numb):
		self._id = id 
		self._t = t 
		self._numb = numb 
		self._queue = None 
		self._wait = None


class EventSimulator(object):
	def __init__(self):
		self._k = HeapPriorityQueue()
		self._isSetk = True
		self._id = 0
		self._t = 0
		self._info_list = []
		self._queueLst = []

	def arriveCustomer(self, id, t, numb):
		if self._t > t:
			raise timeError('You can"t give time less than global time.')

		if numb <= 0:
			raise BurgerError('Why are you here.')

		if self._id + 1 != id :
			raise BaseException('id are not equal')

		else:
			self._id = id
		newCustomer = Customer(id, t, numb)
		self._info_list.append(newCustomer)
		pass

	def actualMinQueue(self, item):
		for l in range(item[1][0]):
			# print(len(self._queueLst[l]), len(item[1][1]), item[1][0])
			if len(self._queueLst[l]) == len(item[1][1]):
				return (len(self._queueLst[l]), (l + 1, self._queueLst[l]))

	def advanceTime(self, t):
		person = self._info_list[0]
		# print(person)
		arrivalTime = person._t

		i = 0
		while arrivalTime <= t:

			# print(arrivalTime, queueTime)
			# print(queueTime)
			# print(i, 'hiii')
			queueTuple = self._k.min()
			length, tup  = self.actualMinQueue(queueTuple)
			minQueue = tup[1]
			queueTime = tup[0]
			
			if person._queue:
				# queueTime = person._queue[0]
				if (arrivalTime + queueTime) < t:
					# print(self._k.min(), 'dequeue ke pahle')
					person._queue[1].dequeue()
					# minQueue = self._k.min()[1][1]
					
					self._k.update_key(minQueue, len(minQueue))
					# print(self._k.min(), 'dequeue ke time', len(minQueue))
					print('dequeue from queue number', person._queue[0], 'and id is', person._id)
					# i += 1
				i += 1

			elif arrivalTime <= t:
				# minQueue = self._k.min()[1][1]
				person._queue = self.actualMinQueue(queueTuple)[1]
				# print(minQueue)
				# print(self._k.min(), 'enque ke pahle')
				minQueue.enqueue(person)
				# print(person._queue)
				
				self._k.update_key(minQueue, len(minQueue))
				# print(self._k.min(), 'enque ke baad', len(minQueue))
				print('enter in queue', person._queue[0], 'and id is', person._id)


			try:
				person = self._info_list[i]
				arrivalTime = person._t

			except :
				break

			# if (arrivalTime + queueTime) < t:
			# 	if person._queue is not None:
			# 		person._queue.dequeue()
			# 		minQueue = self._k.min()[1][1]
			# 		self._k.update_key(minQueue, len(minQueue))
			# 		print('enter in dequeue', queueTime, 'and id is', person._id)

				# else:
				# 	# minQueue = self._k.min()[1][1]
				# 	# minQueue.enqueue(person)
				# 	# minQueue.dequeue()
				# 	pass

			# tempQueue = minQueue
			# tempTime = person._queue[0]
			# # print('temp time', tempTime)
			# for j in range(tempTime):
			# 	if len(self._queueLst[j]) <= tempTime:
			# 		tempTime = len(self._queueLst[j])
			# 		tempQueue = self._queueLst[j]

			# queueTime = tempTime
			# minQueue = tempQueue
			# print(minQueue, 'after')
			
			
			# else:
			# 	i += 1

			 


	def waitInQueue(self, queue, queueNumber, customer):
		t = 0  

		queue.enqueue(customer)
		print('Enter in queue', queueNumber)
		self._k.update_key(queue, len(queue))
		while t <= queueNumber:
			t += 1 
			pass

		queue.dequeue()


	def setM(self, m):
		pass

	def setK(self, k):
		if not self._isSetk:
			raise BaseException('Error hai bhai baar baar k ko change mat kar, rahane de ab.')

		self._isSetk = False
		
		for i in range(k):
			s = Queue()
			self._k.add(len(s), (i+1, s))
			self._queueLst.append(s)
		pass

	def isEmpty(self):
		pass

obj = EventSimulator()
print(obj)

obj.arriveCustomer(1, 5, 4)
obj.arriveCustomer(2, 10, 4)
obj.arriveCustomer(3, 11, 4)
obj.arriveCustomer(4, 12, 4)


# print(obj._info_list[0]._numb)


# obj.setK(1)
obj.setK(2)

# print(obj._k.min())
# print(obj._queueLst)


obj.advanceTime(12)