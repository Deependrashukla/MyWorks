def response():
	response = int(input())
	i = response
	while response != -1:
		response = int(input())
		if response >=i :
			i = response
	return i,1

print(response())