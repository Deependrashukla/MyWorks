call_frame = 0

def fabonacii(n):
	global call_frame

	if n <= 1 :
		return 1

	call_frame += 1

	return fabonacii(n - 1) + fabonacii(n - 2)

print(fabonacii(30), call_frame)