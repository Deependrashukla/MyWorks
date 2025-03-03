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
	# print(dic)

	return dic

def add_word(word, dic):
	if not word in dic :
		dic[word] = 1

	else:
		dic[word] += 1

def load_file(fname1, fname2):

	loader1 = wordcount(fname1)
	loader2 = wordcount(fname2)
	result = {}

	while (not loader1 is None) or (not loader2 is None) :
		if not loader1 is None:
			try:
				amount = next(loader1)
				print('Loaded' + str(amount) + '% of' + repr(fname1))

			except StopIteration as e:
				result.update(e.args[0])
				loader1 = None

		if not loader2 is None:
			try:
				amount = next(loader2)
				print('Loaded' + str(amount) + '% of' + repr(fname2))

			except StopIteration as e:
				result.update(e.args[0])
				loader2 = None


	return 'The the len of text ' + str(len(result))

print(load_file('C:/Users/kirtan/Downloads/gandhi10.txt','C:/Users/kirtan/Downloads/gandhi.txt'))

# print(wordcount('C:/Users/kirtan/Downloads/gandhi.txt'))