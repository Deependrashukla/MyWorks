
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
		# self.k = 0
		# self.m = 0
		self._id = 0
		self._t = 0
		self._info_list = []



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

	def advanceTime(t):
		pass

	def setM(m):
		pass

	def setK(k):
		pass

	def isEmpty(self):
		pass

obj = EventSimulator()
print(obj)

obj.arriveCustomer(1, 2, 4)
print(obj._info_list[0]._numb)