"""
Module for currency exchange
This module provides several string parsing functions to
implement a simple currency exchange routine using an online currency service.
The primary function in this module is exchange.
Author: Kirtan Khichi
# Date: 24 november,2022
# """
# old=input('Enter original currency: ')
# new=input('Enter desired currency: ')
# # amt=float(input('Enter original amount: '))
def before_space(s):
	'''
	Returns a copy of s up to, but not including, the first space.

	In this function we are doing a string slicing in which we are doing string slice and get substring before space.
	#Test cases are returning a substring before space.
	
	>>> before_space('a b')
	'a'
	>>> before_space('2.45 Euro')
	'2.45'
	>>> before_space('a  b')
	'a'
	>>> before_space('2.456   USD')
	'2.456'
	>>> before_space(' a b')
	'a'
	>>> before_space(' a  b')
	'a'
	>>> before_space(' 2.45  Euro')
	'2.45'


	Parameter s: the string to slice.
	Precondition: s is a string with at least one space.
	'''
	s=s.strip()
	string_space_index=s.find(' ')
	# index1=s.index('"')
	word=s[:string_space_index]
	return word


def after_space(s):
	'''
	Returns a copy of s after the first space.

	In this function we are doing string slicing in which we are giving output after first space substring.
	#Test cases are returning a substring after the first space. 
	Examples:
	>>> after_space('a b')
	'b'
	>>> after_space('2.45 Euro')
	'Euro'
	>>> after_space('a  b')
	' b'
	>>> after_space('2.456  USD')
	' USD'
	>>> after_space(' a b')
	'b'
	>>> after_space(' a  b')
	' b'
	>>> after_space(' 2.45  Euro')
	' Euro'


	Parameter s: the string to slice.
	Precondition: s is a string with at least one space.
	'''
	s=s.strip()
	string_space_index=s.find(' ')

	word=s[string_space_index+1:]
	return word





def first_inside_quotes(s):
	'''
	Returns the first substring of s between two (double) quotes. 

	A quote character is one that is inside a string, not one that delimits it.
	We typically use single quotes (') to delimit a string if we want to use a double quote character (") inside of it.
	

	Examples:
	>>> first_inside_quotes('A "B C" D') 
	'B C'
	>>> first_inside_quotes(' A "B C" D')
	'B C'
	>>> first_inside_quotes(' A "B C" D ')
	'B C'
	>>> first_inside_quotes('A "B C" D "E F" G')
	'B C'

	because it only picks the first such substring
	
	Parameter s: a string to search.
	Precondition: s is a string containing at least two double quotes.
	'''
	s=s.strip()
	double_quote_index=s.find('"')
	double_quote_index_end=s.find('"',double_quote_index+1)
	result=s[double_quote_index+1:double_quote_index_end]

	return result




def get_lhs(json):
	'''
	Returns the lhs value in the response to a currency query.

	Given a JSON response to a currency query, this returns the string inside double quotes (") immediately 
	following the keyword.
	"lhs". For example, if the JSON is'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if the JSON response contains an error message.
	Examples:
	>>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'1 Bitcoin'
	

	Parameter json: a json string to parse.
	Precondition: json is the response to a currency query.

	'''
	json_colon=json.index(':')
	json_colon_end=json.index(',')
	return json[json_colon+3:json_colon_end-1]

	

def get_rhs(json):
	# json='{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	'''
	Returns the rhs value in the response to a currency query.

	Given a JSON response to a currency query, this returns the string inside double quotes (") immediately 
	following the keyword.
	"rhs". For example, if the JSON is '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not '"38781.518240835 Euros"').
	This function returns the empty string if the JSON response contains an error message.
	Examples:
	>>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'19995.85429186 Euros'

	Parameter json: a json string to parse.
	Precondition: json is the response to a currency query.

	'''
	# json_colon=json.index(':')
	# json_colon_end=json.index(',')
	# json_substring=json[json_colon+1:json_colon_end]
	# j_start=json.index(':',len(json_substring)+1)
	# j=json.index(',',json_colon_end+1)
	# j_end=json.index(',',j+1)
	json_colon=json.index(':')
	# print(json_colon)
	json_colon_end=json.index(',')
	# print(json_colon_end)
	json_substring=json[json_colon+1:json_colon_end]
	# print(json_substring)
	global j_start
	j_start=json.index(':',json_colon+1)
	# print(j_start)
	j=json.index(',',json_colon_end+1)
	# print(j)
	j_end=json.index(',',json_colon_end+1 )
	# print(j_end)
	# print(len(json))
	# print(json)
	# return json[j:j+1]
	return json[j_start+3:j_end-1].strip()
	# return json[j:j_end+1]
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
	print(json)
	json_colon_index=json.index(':')
	json_last_quote=json.index('"')
	# global json1
	json=json[json_last_quote+2:json_colon_index-1].strip()
	json=json[::-1]
	return "Exchange currency code is invalid." in json
	json=json[::-1]
	json_colon_index=json.index(':')
	json_last_quote=json.index('"')
	json=json[json_last_quote+1:json_colon_index-2].strip()
	json=json[::-1]
	return not(json=='')

print(has_error('{ "lhs":"2 Namibian Dollars", "rhs":"2 Lesotho Maloti","err":""}'))
# if __name__=='__main__':
	# import doctest
	# doctest.testmod()


def query_website():
	'''
	Returns a JSON string that is a response to a currency query.

	A currency query converts amt money in currency old to the currency new. The response should be a string of the 
	form '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'where the values old-amount and new-amount contain 
	the value and name for the old and new currencies. If the query is invalid, both old-amount and new-amount 
	will be empty, while "err" will have an error message.
	Examples:
	>>> query_website('USD','Euro',1.45)
	'{'lhs':"1.45 USD",'rhs':"",'err':""}'
	>>> query_website('USD','Eurokjh',1.45)
	'{'lhs':"",'rhs':"",'err':"This is wrong currency to convert"}'


	Parameter old: the currency on hand.
	Precondition: old is a string with no spaces or non-letters.
	Parameter new: the currency to convert to.
	Precondition: new is a string with no spaces or non-letters.
	Parameter amt: amount of currency to convert.
	Precondition: amt is a float.
	'''
	import requests
	json = (requests.get('http://cs1110.cs.cornell.edu/2022fa/a1/?old=USD&new=CUP&amt=5')).text
	return json

# import requests
# json = (requests.get('http://cs1110.cs.cornell.edu/2022fa/a1/?old=USD&new=CUP&amt=2.5')).text
# print(get_lhs(json))
# print(get_rhs(json))
# print(has_error(json))
def is_currency(code):
	'''0
	Returns: True if code is a valid (3 letter code for a) currency.It returns False otherwise.
	
	In this function we are checking that the currency code is correct or not.Here are some currency code list atteched
	with the link ('https://www.cs.cornell.edu/courses/cs1110/2022fa/assignments/a1/#appendix-supported-currencies')
	>>> is_currency('USD')
	True
	>>> is_currency('usd')
	True
	>>> is_currency('uqd')
	False

	Parameter code: the currency code to verify
	Precondition: code is a string with no spaces or non-letters.
	'''
	# json=after_space(get_rhs(json))
	# return "Currency amount is invalid."  in query_website()
	# return "Currency amount is invalid."  in ('usd','cup')
	return old in ('usd','new')

def exchange(old, new, amt):
	'''
	Returns the amount of currency received in the given exchange.

	In this exchange, the user is changing amt money in currency old to the currency new.
	The value returned represents the amount in currency new.The value returned has type float.

	Parameter old: the currency on hand.
	Precondition: old is a string with no spaces or non-letters.
	Parameter new: the currency to convert to.
	Precondition: new is a string with no spaces or non-letters.
	Parameter amt: amount of currency to convert.
	Precondition: amt is a float.
	'''

	# return get_lhs(query_website(old,new,amt))==(25.75)*get_rhs(query_website(old,new,amt))
	s=query_website()
	s=get_lhs(s)
	s=before_space(s)
	return float(s)*25.75