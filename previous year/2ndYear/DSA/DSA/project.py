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


class EventSimulator(object):
	def __init__(self):
		self._k = HeapPriorityQueue()
		self._isSetk = True
		# self.m = 0
		self._id = 0
		self._t = 0
		self._info_list = []
		self._globalTime = 0
		self._tempLst = []

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

	def advanceTime(self, t):
		value = self._info_list[0]
		temp = value._t
		j = 0
		# self._k[0].push(value)
		i = 0
		while temp <= t:
			minimium = self._k.min()[1][1]
			k_index_queue = self._k.min()[1][0]
			# minimium.enqueue(value)
			# self.waitInQueue(minimium, self._k.min()[1][0], value)
			# print(self._k.data)
			# print(len(minimium))
			# self._k.update_key(minimium, len(minimium))
			print('enter in queue', k_index_queue, 'and id is', value._id)
			# print(self._k.min())
			# self._k.min()[0] = len(minimium)
			# waitInQueue(minimium, self._k.min()[1][0], )
			# print(self._k.min(), len(minimium))
			
			i += 1

			try:

				value = self._info_list[i]
				temp = value._t

			except :
				break 

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
			self._tempLst.append(s)
		pass

	def isEmpty(self):
		pass

obj = EventSimulator()
print(obj)

obj.arriveCustomer(1, 2, 4)
obj.arriveCustomer(2, 3, 4)
obj.arriveCustomer(3, 7, 4)
obj.arriveCustomer(4, 8, 4)

print(obj._info_list[0]._numb)


obj.setK(1)
# obj.setK(6)

print(obj._k.min())
print(obj._tempLst)


obj.advanceTime(11)