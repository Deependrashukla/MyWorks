def wordcount(fname):
	file = open(fname)
	text = file.read()
	file.close()
	dic = {}
	word = ''

	for pos in range(len(text)) :

		if pos % (len(text) // 10) == 0:
			yield round(100 * pos / len(text))

		x = text[pos]
		if x.isalpha():
			word = word + x 

		else:
			if word != '':
				add_word(word,dic)

			word = ''

	if word != '':
		add_word(word, dic)
	print(dic)

	return dic

def add_word(word, dic):
	if not word in dic :
		dic[word] = 1

	else:
		dic[word] += 1

def load_file(fname):

	loader = wordcount(fname)
	result = None

	while not loader is None:
		try:
			amount = next(loader)
			print('Loaded' + str(amount) + '% of' + repr(fname))

		except StopIteration as e:
			result = e.args[0]
			loader = None


	# return 'The the len of text' + str(len(count))

print(load_file('C:/Users/kirtan/Downloads/gandhi10.txt'))

# print(wordcount('C:/Users/kirtan/Downloads/gandhi.txt'))