class Next2iter(object):

	@property
	def limit(self):
		return self._limit

	def __init__(self, l):

		self._limit = l
		self._pos = 0


	def __next__(self):

		if self._pos >= self._limit:
			#raise StopIteration()
			raise StopIteration("game over","rttyh","kirtan-->--->" ) 

		else:
			value = self._pos * self._pos
			self._pos += 1
			return value

class range2(object):
	def __init__(self, n):
		self._limit = n

	def __iter__(self):
		return Next2iter(self._limit)

	# def __str__(self):
	# 	return str(Next2iter(self._limit))
# s = range(5)
w = Next2iter(5)
# w = iter(w)
for i in w:
	print(i)
# print(s)
# print(w)
# print(list(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))

# k = Next2iter(5) 
# print(list(k))
# print(k)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

# k = iter((1, 2, 3)
# print(k)
# print(next(k), next(k), next(k), next(k))
# print(help(iter))