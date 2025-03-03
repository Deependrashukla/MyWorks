def choices_helper(value):
	x = True
	for i in value:
		if type(i) != str:
			x = False

	return x 

class Question(object):
	"""
	A class representing a question in the lab system
	Attribute USED_INDICES: A CLASS ATTRIBUTE list of all question indices. 
	This list starts off empty, as there are no questions to start with.
	"""
	# ATTRIBUTE _index: The question index. An int > 0 (IMMUTABLE).
	# ATTRIBUTE _text: The question wording. A nonempty string (MUTABLE).

	USED_INDICES = []

	@property 
	def index(self):
		return self._index


	@property
	def text(self):
		return self._text


	@text.setter
	def text(self, value):
		assert type(value) == str, str(value) + ' is not an string.'
		assert len(value) != 0, value + ' must be non empty.'

		self._text = value 


	def __init__(self, i, t):
		# global USED_INDICES
		assert type(i) and i > 0, ' index must be int and > 0.'

		self.text = t
		self._index = i

		Question.USED_INDICES.append(i)


	def __str__(self):
		return str(self.index) + '.' + self.text 


	def __eq__(self, other):
		return type(self) == type(other) and (self.index == other.index)


class MCQ(Question):
	"""
	A class representing a multiple choice question.
	"""

	# ATTRIBUTE _choices: The options. A nonempty tuple of strings. (MUTABLE)
	# ATTRIBUTE _correct: The index of the correct answer. An int. (MUTABLE)
	# ADDITIONAL INVARIANT: _correct is a valid index of _choices at all times
	# HINT: This allows _correct to be negative as long as it is in bounds
	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.

	@property
	def choices(self):
		return self._choices

	@property
	def correct(self):
		return self._correct


	@choices.setter
	def choices(self, value):
		assert type(value) == tuple, str(value) + ' is not an tuple.'
		assert len(value) != 0, str(value) + ' has to non-empty tuple.'
		assert choices_helper(value) 
		self._choices = value


	@correct.setter 
	def correct(self, value): 
		assert type(value) == int 
		assert value in Question.USED_INDICES , str(value) + ' is not valid index.'
		self._correct = value 

	

	def __init__(self, i, t, ch, c): 
		"""
		Initializes a new multiple choice question with given choices.

		Precondition: index is an int > 0, and not already in use.
		That is, index cannot be an element of USED_INDICES in Question.
		Precondition: text is a non-empty string
		Precondition: choices is a nonempty tuple of strings
		Precondition: correct is an int and a valid index of choices
		(OPTIONAL ATTRIBUTE; correct is -1, the last choice, by default)
		"""
		print(type(self))

		super().__init__(i, t) 
		print(type(self))
		self.choices = ch 
		self.correct = c

	def __str__(self): 
		"""
		Returns a string representation of this multiple choice question.

		The format is '<index>. <text> <answer>'. 

		For example, suppose the question with index 2 and text 'What is your quest?' 
		has choices ('To pass this exam.', 'To seek the Holy Grail.'). 
		If correct is 1, then the string is '2. What is your quest? To seek the Holy Grail.' 
		"""

		return str(self.index) + '. ' + self.text + ' ' + str(self.choices[self.correct]) 



a = Question(1, 'What is your name?')

print(a)

b = Question(2, 'What is your age?')

print(b)

print(a == b)
# print(Question.USED_INDICES)

c = MCQ(2, 'what is your age?', ('0', 'Kirtan', '19',), 2)

print(c)

print(Question.USED_INDICES)

print(getattr(c, 'index'))

print(c.__dict__)