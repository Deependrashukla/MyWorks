# a, b, i = 0, 1, 0
# while i < 5 :
# 	b, a = a + b, b
# 	print(b)
# 	i += 1


i = 1
while i <= 100 :
	if i % 2 == 0:
		continue

	print(i,end='')
	i += 1
	