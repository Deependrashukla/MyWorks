def move(n, src, dst, tmp):
	if n >= 1:
		move(n - 1, src, tmp, dst)
		print((src, dst))
		move(n - 1, src, dst, tmp)

move(3, 1, 3, 2)