class SingalNode(object):
	def __init__(self):
		self._element = None
		self._reference = None


	@property
	def next1(self):
		return self._reference

	@next1.setter
	def next1(self, reference):
		self._reference = reference

	@property
	def element(self):
		return self._element

	@element.setter
	def element(self, ele):
		self._element = ele 
