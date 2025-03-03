def last_name_first(name):
	'''
	>>> last_name_first('sitare foundation')
	'foundation,sitare'
	>>> last_name_first('sitare  foundation')
	'foundation, sitare'
	'''
	end_first=name.find(' ')
	print(end_first)
	first=name[:end_first]
	print(first)
	last=name[end_first+1:].strip()
	

	print(last)
	return last+','+first
print(last_name_first('sitare  foundation'))


'''
if __name__=='__main__':
	import doctest
	doctest.testmod()'''