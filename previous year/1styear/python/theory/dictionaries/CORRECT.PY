def fun(k):
	for k1, v1 in k.items():
		del k[k1]
		for k2, v2 in k.items():
			if v1 == v2 :
				return True 

		return False

print(fun({1:10,2:10,3:5}))