class Fraction(object):
	"""docstring for Fraction"""
	def __init__(self, n, d):
		# super(Fraction, self).__init__()
		self._numerator = n 
		self._denominator = d

	def _mulInt(self, q):
		return Fraction(self._numerator * q, self._denominator)

	def _mulFrac(self, q):
		return Fraction(self._numerator * q._numerator, self._denominator * q._denominator)

	def __mul__(self, q):
		# assert type(q) == int

		if type(q) == Fraction :

			# self._mulFrac(q)

			return self._mulFrac(q)
		# top = self._numerator * q._numerator
		# bottom = self._denominator * q._denominator

		elif type(q) == int :
			return self._mulInt(q)
		# return Fraction(top, bottom)

	def __rmul__(self, q):
		# assert type(q) == int

		if type(q) == Fraction :

			# self._mulFrac(q)

			return self._mulFrac(q)
		# top = self._numerator * q._numerator
		# bottom = self._denominator * q._denominator

		elif type(q) == int :
			return self._mulInt(q)
		# return Fraction(top, bottom)


	def __eq__(self, q):
		if type(q) != Fraction:
			return False

		left = self._numerator * q._denominator
		right = self._denominator * q._numerator

		return right == left

	def __add__(self, q):
		assert type(q) == Fraction
		bottom = self._denominator * q._denominator
		top = self._numerator * q._denominator + self._denominator * q._numerator

		return Fraction(top, bottom)

	def __le__(self, q):

		left = self._numerator * q._denominator
		right = self._denominator * q._numerator

		return right <= left


	def __lt__(self, q):

		left = self._numerator * q._denominator
		right = self._denominator * q._numerator

		return right < left

	# def __str__(self):
		# return 

	def __str__(self):
		"""
		Return: The string representation of class.
		"""
		return (str(self._numerator) + '/' + str(self._denominator))
