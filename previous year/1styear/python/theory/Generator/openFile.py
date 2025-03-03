def func(filename):
	file = open(filename)
	for line in file:
		line = line[:-1]
		print(line)

	file.close()
# print(func('C:/Users/kirtan/Documents/python/theory/classes/date.py'))
print(func('file1.py'))