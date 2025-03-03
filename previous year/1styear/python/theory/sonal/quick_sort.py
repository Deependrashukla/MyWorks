def partition(b, h, k):
	i = h 
	j = k
	pivot = b[h]

	while i < j:
		if pivot > b[i+1]:
			# print(i)
			b[i + 1], b[i] = b[i], b[i + 1]
			i += 1

		else:
			# print(i,j)
			b[i+1], b[j] = b[j], b[i+1]
			j -= 1
	return i

def quick_sort(b, h, k):
	
	if k - h < 1:
		return 

	j = partition(b, h, k)
	print(b,j)

	quick_sort(b, h, j - 1)
	quick_sort(b, j + 1, k)


lst = [4,7,2,1,5,3]
quick_sort(lst, 0, len(lst)-1)
print(lst)

class A:
	def __init__(self):
		print('dgrgrsrth')
class B(A):
	pass
# class C(B):
	# pass
c = B()