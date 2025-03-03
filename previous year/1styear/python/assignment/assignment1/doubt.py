# # # if True:
# # 	# print('hii')
# # def before_space(s):
# # 	'''
# # 	Returns a copy of s up to, but not including, the first space.

# # 	In this function we are doing a string slicing in which we are doing string slice and get substring before space.
# # 	#Test cases are returning a substring before space.
	
# # 	>>> before_space('a b')
# # 	'a'
# # 	>>> before_space('2.45 Euro')
# # 	'2.45'
# # 	>>> before_space('a  b')
# # 	'a'
# # 	>>> before_space('2.456   USD')
# # 	'2.456'
# # 	>>> before_space(' a b')
# # 	'a'
# # 	>>> before_space(' a  b')
# # 	'a'
# # 	>>> before_space(' 2.45  Euro')
# # 	'2.45'


# # 	Parameter s: the string to slice.
# # 	Precondition: s is a string with at least one space.
# # 	'''
# # 	s=s.strip()
# # 	string_space_index=s.find(' ')
# # 	# index1=s.index('"')
# # 	word=s[:string_space_index]
# # 	# print(word)
# # 	return word

# # def get_lhs(json):
# 	'''
# 	Returns the lhs value in the response to a currency query.

# 	Given a JSON response to a currency query, this returns the string inside double quotes (") immediately 
# 	following the keyword.
# 	"lhs". For example, if the JSON is'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
# 	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
# 	This function returns the empty string if the JSON response contains an error message.
# 	Examples:
# 	>>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
# 	'1 Bitcoin'
	

# 	Parameter json: a json string to parse.
# 	Precondition: json is the response to a currency query.

# 	'''
# 	# json_colon=json.index(':')
# 	# json_colon_end=json.index(',')
# 	# return json[json_colon+3:json_colon_end-1]
# # print(get_lhs('{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'))
# # # print(type(float(before_space(get_lhs('{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }')))))
# print(('a','b') in ('ak','bk'))
# print('a' in 'ak' or 'b' in 'bk')
# print(('a','b') in ('ak','bk',('a','b')))
'''
def incr(x):
	return x+1
if __name__=='__main__':
	print(incr(5))'''
def has_error(json):
	'''
	Returns True if the query has an error; False otherwise.

	Given a JSON response to a currency query, this returns True if there is an error message. 
	For example, if the JSON is '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It does NOT return the message 'Currency amount is 
	invalid.').
	Examples:
	>>> has_error('{ "lhs":"2 Namibian Dollars", "rhs":"2 Lesotho Maloti","err":""}')
	False
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Exchange currency code is invalid." }')
	True

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	'''
	# return json['err']

	
	json=json[::-1]
	# print(json)
	json_colon_index=json.index(':')
	json_last_quote=json.index('"')
	# global json1
	json=json[json_last_quote+2:json_colon_index-1].strip()
	json=json[::-1]
	print(json)
	return "Exchange currency code is invalid." in json
print(has_error())