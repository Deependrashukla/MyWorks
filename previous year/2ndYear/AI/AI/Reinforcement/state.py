class State(object):

	def __init__(self):
		self._parent = None
		self._child = None
		self._lst = [None] * 9
		self._value = 0


	def getChild(self):
		return self._child

	def setChild(self, ref):
		self._child = ref

	def getParent(self):
		return self._parent

	def setParent(self, ref):
		self._parent = ref

	def enterValue(self, index, value):
		# index = 3 * i + j 
		self._lst[index] = value 

	def getState(self):
		return self._lst

	def getValue(self):
		self._value 

	def setValue(self, value):
		self._value = value

class Tree(object):
	def __init__(self):
		self._startNode = []
		self._valueList = []